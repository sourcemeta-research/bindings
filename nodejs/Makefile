all: .always
	mkdir -p generated/include
	sed -e 's/@PROJECT_VERSION@/0.0.0/g' -e 's/#cmakedefine/#undef/g' \
		../vendor/core/vendor/uriparser/src/UriConfig.h.in \
		> generated/include/UriConfig.h
	cmake \
		-DPROJECT_SOURCE_DIR=../vendor/core \
		-DOFFICIAL_RESOLVER_INPUT=../vendor/core/src/core/jsonschema/official_resolver.in.cc \
		-DOFFICIAL_RESOLVER_OUTPUT=./generated/official_resolver.cc \
		-P ../vendor/core/src/core/jsonschema/official_resolver.cmake
	npm install --verbose --build-from-source
	npm test

.always:
