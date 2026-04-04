module Jekyll
  module VenueName
    def venue_name(input)
      site = @context.registers[:site]
      return site.data.fetch('venues', {}).transform_keys(&:downcase).fetch(input.to_s.downcase, {}).fetch('name', input)
    end
  end
end

Liquid::Template.register_filter(Jekyll::VenueName)