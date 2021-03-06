
SHELL := /bin/bash
.PHONY: help


## Show help
help:
	@echo ''
	@echo 'Usage:'
	@echo "${YELLOW} make ${RESET} ${GREEN}<target> [options]${RESET}"
	@echo ''
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-\_0-9]+:/ { \
    	message = match(lastLine, /^## (.*)/); \
		if (message) { \
			command = substr($$1, 0, index($$1, ":")-1); \
			message = substr(lastLine, RSTART + 3, RLENGTH); \
			printf "  ${YELLOW_S}%-$(TARGET_MAX_CHAR_NUM)s${RESET} %s\n", command, message; \
		} \
	} \
    { lastLine = $$0 }' $(MAKEFILE_LIST)
	@echo ''

## create container for development
dev:
	docker-compose up --build --force-recreate --remove-orphans --detach

## remove container
tear-dev:
	docker-compose down -v

## remove pycache files
clean:
	find . -path "*/__pycache__/*.py" -not -name "__init__.py" -delete; find . -path "*/__pycache__/*.pyc"  -delete

## Start the prod environment
prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --detach --build --force-recreate --remove-orphans

## Run CI tests.
test:
	docker-compose up --build --force-recreate --remove-orphans --detach
	docker-compose run swift_writers coverage erase --rcfile=.coveragerc
	docker-compose run swift_writers coverage run --rcfile=.coveragerc manage.py test
	docker-compose run swift_writers coverage report --rcfile=.coveragerc
	docker-compose run swift_writers coverage html --rcfile=.coveragerc

test-local:
	source .env; cd app; coverage erase --rcfile=.coveragerc; coverage run --rcfile=.coveragerc manage.py test; coverage report --rcfile=.coveragerc; coverage html --rcfile=.coveragerc

## run server locally
runserver:
	source dev.env; cd app; python manage.py set_essays_cache; python manage.py set_academic_levels_cache; python manage.py makemigrations; python manage.py migrate; python manage.py runserver localhost:8080

ifeq (test,$(firstword $(MAKECMDGOALS)))
  TAG_ARGS := $(word 2, $(MAKECMDGOALS))
  $(eval $(TAG_ARGS):;@:)
endif

# COLORS
GREEN  := `tput setaf 2`
YELLOW := `tput setaf 3`
WHITE  := `tput setaf 7`
YELLOW_S := $(shell tput -Txterm setaf 3)
NC := "\e[0m"
RESET  := $(shell tput -Txterm sgr0)

INFO := @bash -c 'printf $(YELLOW); echo "===> $$1"; printf $(NC)' SOME_VALUE
SUCCESS := @bash -c 'printf $(GREEN); echo "===> $$1"; printf $(NC)' SOME_VALUE