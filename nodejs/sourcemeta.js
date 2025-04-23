const addon = require('bindings')('sourcemeta');

console.log(addon.lint({
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": [ "string" ]
}));
