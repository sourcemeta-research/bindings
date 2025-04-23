#include <napi.h>

#include <sourcemeta/core/json.h>
#include <sourcemeta/core/jsonschema.h>
#include <sourcemeta/core/alterschema.h>

#include <sstream>

static auto binding_lint(const Napi::CallbackInfo& info) -> Napi::String {
  Napi::Env env = info.Env();
  Napi::Object json = env.Global().Get("JSON").As<Napi::Object>();
  Napi::Function stringify = json.Get("stringify").As<Napi::Function>();
  Napi::Object schema = info[0].As<Napi::Object>();
  Napi::String schema_stringified = stringify.Call(json, { schema }).As<Napi::String>();
  const std::string schema_string = schema_stringified.ToString().Utf8Value();
  const auto value{sourcemeta::core::parse_json(schema_string)};

  sourcemeta::core::SchemaTransformer bundle;
  sourcemeta::core::add(bundle,
                        sourcemeta::core::AlterSchemaCategory::AntiPattern);
  sourcemeta::core::add(bundle,
                        sourcemeta::core::AlterSchemaCategory::Simplify);
  sourcemeta::core::add(bundle,
                        sourcemeta::core::AlterSchemaCategory::Superfluous);
  sourcemeta::core::add(bundle,
                        sourcemeta::core::AlterSchemaCategory::Redundant);
  sourcemeta::core::add(bundle,
                        sourcemeta::core::AlterSchemaCategory::SyntaxSugar);

  const auto subresult{bundle.check(value,
    sourcemeta::core::schema_official_walker,
    sourcemeta::core::schema_official_resolver, 
    [](const auto &pointer, const auto &name, const auto &message) {

    }
  )};

  if (!subresult) {
    return Napi::String::New(env, "INVALID");
  }

  std::ostringstream result;
  sourcemeta::core::stringify(value, result);
  return Napi::String::New(env, result.str());
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "lint"),
              Napi::Function::New(env, binding_lint));
  return exports;
}

NODE_API_MODULE(sourcemeta, Init)
