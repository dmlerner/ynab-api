1. Download official spec:

```
wget https://api.youneedabudget.com/papi/spec-v1-swagger.json
```

2. Convert from swagger to openapi 3:

```
java -jar ./swagger-codegen-cli-3.0.29.jar generate -l openapi -i spec-v1-swagger.json -o .
```

3. Mark non-required fields as nullable.

```
python patch-openapi-json.py < openapi.json > openapi-patched.json
```

4. Generate api:

```
java -jar openapi-generator-cli.jar generate -i openapi-patched.json -g python --enable-post-process-file \
  --package-name ynab_api --git-user-id dmlerner --git-repo-id ynab-api -p 'infoName=David Lerner'
```

5. Optionally, format:

```
yapf -ir **/*.py
```
