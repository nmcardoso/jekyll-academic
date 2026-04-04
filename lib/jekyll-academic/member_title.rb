module Jekyll
  class MemberTitle < Generator
    def generate(site)
      if site.collections.has_key?('members') then
        site.collections['members'].docs.each do |member|
          member.data['title'] = member.data['name']
        end
      end
    end
  end
end