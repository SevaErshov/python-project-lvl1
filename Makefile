install: 
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install: #установка пакета в пользовательское окружение
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

 
