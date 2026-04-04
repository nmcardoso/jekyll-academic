module Jekyll
  module VenueName
    def venue_name(input)
      return nil if input.nil?
      site = @context.registers[:site]
      Jekyll.logger.info "VenueName:", "Venue: #{input}, Data: #{site.data.fetch('venues')}"
      site.data.fetch('venues', {}).transform_keys(&:downcase).fetch(input.downcase, {}).fetch('name', input)
    end
  end
end

Liquid::Template.register_filter(Jekyll::VenueName)