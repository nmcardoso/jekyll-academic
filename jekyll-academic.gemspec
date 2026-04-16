Gem::Specification.new do |spec|
  spec.name          = "jekyll-academic"
  spec.version       = "0.4.0"
  spec.authors       = ["Natanael M. Cardoso"]
  spec.email         = ["contact@natanael.net"]

  spec.summary       = "A personal academic Jekyll site"
  spec.description   = "A Jekyll-based academic website with blog, publications, people, and news collections."
  spec.homepage      = "https://natanael.net"
  spec.required_ruby_version = ">= 3.0"

  spec.metadata["plugin_type"] = "theme"

  spec.files = Dir.glob("**/*", File::FNM_DOTMATCH).reject do |path|
    File.directory?(path) ||
      path.start_with?(".git/", ".github/", ".jekyll-cache/", ".venv/", "_site/", "node_modules/", "test_personal/") ||
      path.end_with?(".gem") ||
      path == "." ||
      path == ".."
  end

  spec.require_paths = ["lib"]

  spec.add_runtime_dependency "jekyll", "~> 4.4.1"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.12"
  spec.add_runtime_dependency "jekyll-include-cache"
  spec.add_runtime_dependency "jekyll-sitemap"
  spec.add_runtime_dependency "jekyll-gist"
  spec.add_runtime_dependency "jekyll-sass-converter"
  spec.add_runtime_dependency "jekyll-scholar"
  spec.add_runtime_dependency "jekyll-seo-tag"
  spec.add_runtime_dependency "jekyll-paginate-v2"
  spec.add_runtime_dependency "jekyll-archives"
  spec.add_runtime_dependency "jekyll-academic"

  spec.add_development_dependency "bundler"
  spec.add_development_dependency "rake"
end