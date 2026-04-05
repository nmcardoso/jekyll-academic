# Generator to create bidirectional references between publications and members
# - Adds `page.data['members_objects']` (array of member docs) to each publication
# - Adds `member.data['publications']` (array of publication docs) to each member
# Matching logic:
# - Each member can provide `other_names` in front matter (array or string)
# - Each publication has `members` (string or array). The string may contain names
#   separated by commas and/or the word "and"; we normalize and split it.

module Jekyll
  class PublicationBackrefsGenerator < Generator
    safe true
    priority :low

    def generate(site)
      members_collection = site.collections['members']
      pubs_collection = site.collections['publications']

      return unless members_collection && pubs_collection

      members = members_collection.docs
      pubs = pubs_collection.docs

      mapping = build_citation_mapping(members)

      # initialize publications lists on members
      members.each do |a|
        a.data['publications'] = []
      end

      pubs.each do |pub|
        matched_members = []

        names = extract_member_names(pub.data['authors'])

        names.each do |name|
          norm = normalize_name(name)
          
          if mapping.key?(norm)
            mapping[norm].each do |member_doc|
              unless matched_members.include?(member_doc)
                matched_members << member_doc
              end
              # add pub to member.publications if not already
              member_doc.data['publications'] << pub unless member_doc.data['publications'].include?(pub)
            end
          else
            Jekyll.logger.debug "PublicationBackrefs:", "no match for '#{name}' in pub #{pub.relative_path}"
          end
        end

        pub.data['members'] = matched_members
      end

      Jekyll.logger.info "PublicationBackrefs:", "linked #{pubs.count} publications and #{members.count} members"
    end

    private
    
    def build_citation_mapping(members)
      mapping = {}
      members.each do |a|
        raw = a.data['other_names']
        arr = []
        if raw.is_a?(String)
          arr = [raw]
        elsif raw.is_a?(Array)
          arr = raw
        end
        if a.data['name'] != nil and not arr.include?(a.data['name'])
          arr << a.data['name']
        end 
        # fallback: use basename without ext as a citation string
        if arr.empty?
          arr = [a.basename_without_ext]
        end

        # include alternative names incluing only first letter of the first name
        unless arr.empty?
          alternative = []
          arr.each do |i|
            name = i.split(' ')[0]
            short_name = i.gsub(name, name[0])
            if name.size > 0 and not arr.include?(short_name)
              alternative << short_name
            end
          end

          if alternative.size
            arr = arr + alternative
          end
        end

        arr.each do |c|
          key = normalize_name(c)
          mapping[key] ||= []
          mapping[key] << a unless mapping[key].include?(a)
        end
      end
      mapping
    end

    def extract_member_names(members_field)
      return [] if members_field.nil?
      if members_field.is_a?(Array)
        return members_field.map(&:to_s).map(&:strip).reject(&:empty?)
      end
      s = members_field.to_s
      # Normalize separators: ' and ' -> ',', also handle semicolons
      s = s.gsub(/\s+and\s+/i, ',')
      s = s.gsub(/\s*;\s*/, ',')
      parts = s.split(',').map(&:strip).reject(&:empty?)
      parts
    end

    def normalize_name(s)
      return '' if s.nil?
      str = s.to_s
      # Replace NBSP, remove dots, downcase, collapse whitespace
      str = str.gsub("\u00A0", ' ')
      str = str.gsub('.', '')
      str = str.downcase.strip
      str = str.gsub(/\s+/, ' ')
      str
    end
  end
end