THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help voting-backend-up
help:
				make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

voting-backend-up:
	docker compose -f docker/local.yaml --project-directory . up $(args)

voting-backend-down:
	docker compose -f docker/local.yaml --project-directory . down

web-graphene-export-schema:
	docker compose -f docker/local.yml --project-directory . run --rm django python manage.py graphql_schema --schema schema.schema --out /src/frontend/src/graphql/schema.graphql

web-relay-compile:
	docker compose -f docker/local.yml --project-directory . run --rm react zsh -c "yarn relay"