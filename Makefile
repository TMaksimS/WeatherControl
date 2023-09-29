up_test_db:
	docker compose -f docker-compose-local.yaml up -d
make_migrations: up_test_db
	sleep 2 && alembic upgrade head
up_local: make_migrations
	python3 main.py
down_local:
	docker compose -f docker-compose-local.yaml down --remove-orphans

docker_compose_up:
	docker compose -f docker-compose-ci.yaml up -d
logs_server_app: docker_compose_up
	sleep 5 && docker logs app
up_ci: logs_server_app
	sleep 3 && docker logs updater --follow
down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans