require "jekyll"
require_relative "jekyll-academic/data_types"
require_relative "jekyll-academic/env_vars"
require_relative "jekyll-academic/inline_pdf"
require_relative "jekyll-academic/md5"
require_relative "jekyll-academic/member_title"
require_relative "jekyll-academic/notebook"
require_relative "jekyll-academic/pluralize_filter"
require_relative "jekyll-academic/publication_backrefs"
require_relative "jekyll-academic/venue_name"

module JekyllAcademic
  Jekyll::Hooks.register :site, :post_read do |site|
    puts "JekyllAcademic: Custom plugin is active!"
  end
end