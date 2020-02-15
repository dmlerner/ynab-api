#!/usr/bin/env bash

PACKAGE_VERSION=1.0.1
SWAGGER_JSON_URL='https://api.youneedabudget.com/papi/spec-v1-swagger.json'
JSON_FILE_NAME='spec-v1-swagger.json'
PACKAGE_NAME='ynab_api'
PYTHON_SOURCE_DIR='../assistantforynab/env/bin/activate'

main() {
  set -x

  # download latest API as JSON file
  curl "$SWAGGER_JSON_URL" -O "$JSON_FILE_NAME"

  export PYTHON_POST_PROCESS_FILE='/usr/local/bin/yapf -i'

  # necessary otherwise we won't overwrite previous test files
  rm -rf "test/"

  openapi-generator generate -i "$JSON_FILE_NAME" -g python --package-name "$PACKAGE_NAME" --additional-properties=packageVersion="$PACKAGE_VERSION"

  # shellcheck source=/dev/null
  source "$PYTHON_SOURCE_DIR"
  python3 setup.py install
}

[[ ${BASH_SOURCE[0]} == "$0" ]] && main "$@"
