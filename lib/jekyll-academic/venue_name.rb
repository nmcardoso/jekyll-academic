module Jekyll
  module VenueName
    def venue_name(input)
      return nil if input.nil?
      site = @context.registers[:site]
      site.data.fetch('venues', {}).transform_keys(&:downcase).fetch(input.downcase, {}).fetch('name', input)
    end
  end
end

Liquid::Template.register_filter(Jekyll::VenueName)