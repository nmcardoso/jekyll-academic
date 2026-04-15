module Jekyll
  module VenueNameHelper
    def self.lookup(site, input)
      return nil if input.nil?

      site
        .data
        .fetch('venues', {})
        .transform_keys(&:downcase)
        .fetch(input.downcase, {})
        .fetch('name', input)
    end
  end

  module VenueName
    def venue_name(input)
      site = @context.registers[:site]
      VenueNameHelper.lookup(site, input)
    end
  end

  class MetaVenueName < Generator
    safe true
    priority :low

    def generate(site)
      return unless site.collections.key?('publications')

      site.collections['publications'].docs.each do |doc|
        next if doc.data['description']
        next unless doc.data['doi'] && doc.data['venue']

        name = Jekyll::VenueNameHelper.lookup(site, doc.data['venue'])
        doc.data['description'] = "Published in #{name}"
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::VenueName)