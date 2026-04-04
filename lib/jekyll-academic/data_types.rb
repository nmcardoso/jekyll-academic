module Jekyll
  module DataTypes
    def isstring(var)
      var.is_a?(String)
    end

    def isarray(var)
      var.is_a?(Array)
    end
  end
end

Liquid::Template.register_filter(Jekyll::DataTypes)