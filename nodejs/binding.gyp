{
  "targets": [
    {
      "target_name": "sourcemeta",
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      "cflags": [ "-std=c11" ],
      "cflags_cc": [ "-std=c++20" ],
      "sources": [
        "wrapper.cc",

        "../vendor/core/vendor/uriparser/src/UriCommon.c",
        "../vendor/core/vendor/uriparser/src/UriCompare.c",
        "../vendor/core/vendor/uriparser/src/UriEscape.c",
        "../vendor/core/vendor/uriparser/src/UriFile.c",
        "../vendor/core/vendor/uriparser/src/UriIp4.c",
        "../vendor/core/vendor/uriparser/src/UriIp4Base.c",
        "../vendor/core/vendor/uriparser/src/UriMemory.c",
        "../vendor/core/vendor/uriparser/src/UriNormalize.c",
        "../vendor/core/vendor/uriparser/src/UriNormalizeBase.c",
        "../vendor/core/vendor/uriparser/src/UriParse.c",
        "../vendor/core/vendor/uriparser/src/UriParseBase.c",
        "../vendor/core/vendor/uriparser/src/UriQuery.c",
        "../vendor/core/vendor/uriparser/src/UriRecompose.c",
        "../vendor/core/vendor/uriparser/src/UriResolve.c",
        "../vendor/core/vendor/uriparser/src/UriShorten.c",
        "../vendor/core/src/core/uri/uri.cc",
        "../vendor/core/src/core/uri/escaping.cc",
        "../vendor/core/src/core/json/json.cc",
        "../vendor/core/src/core/json/json_value.cc",
        "../vendor/core/src/core/jsonpointer/jsonpointer.cc",
        "../vendor/core/src/core/jsonpointer/position.cc",
        "../vendor/core/src/core/jsonschema/bundle.cc",
        "../vendor/core/src/core/jsonschema/frame.cc",
        "../vendor/core/src/core/jsonschema/jsonschema.cc",
        "../vendor/core/src/core/jsonschema/official_walker.cc",
        "../vendor/core/src/core/jsonschema/resolver.cc",
        "../vendor/core/src/core/jsonschema/transformer.cc",
        "../vendor/core/src/core/jsonschema/walker.cc",
        "./generated/official_resolver.cc",
        "../vendor/core/src/extension/alterschema/alterschema.cc",
      ],
      "include_dirs": [
        "<!@(node -p \"require('node-addon-api').include\")",
        "./generated/include",
        "../vendor/core/vendor/uriparser/include",
        "../vendor/core/vendor/boost-regex/include",
        "../vendor/core/src/core/uri/include",
        "../vendor/core/src/core/regex/include",
        "../vendor/core/src/core/json/include",
        "../vendor/core/src/core/jsonpointer/include",
        "../vendor/core/src/core/jsonschema/include",
        "../vendor/core/src/extension/alterschema/include",
      ],
      "defines": [
        "NAPI_CPP_EXCEPTIONS",
        "URI_STATIC_BUILD",
        "BOOST_REGEX_STANDALONE",
        "SOURCEMETA_CORE_URI_EXPORT=",
        "SOURCEMETA_CORE_JSON_EXPORT=",
        "SOURCEMETA_CORE_JSONPOINTER_EXPORT=",
        "SOURCEMETA_CORE_JSONSCHEMA_EXPORT=",
        "SOURCEMETA_CORE_ALTERSCHEMA_EXPORT="
      ],
      "conditions": [
        ['OS=="mac"', {
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": 'YES',
            "MACOSX_DEPLOYMENT_TARGET": "10.15",
            "CLANG_CXX_LANGUAGE_STANDARD": "c++20",
            "CLANG_CXX_LIBRARY": "libc++"
          }
        }]
      ]
    }
  ]
}
