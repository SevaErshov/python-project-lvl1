install: #делает поэтри инсталл
	poetry install

build: #poetry build
	poetry build

publish: #poetry publish для отладки
	poetry publish --dry-run

package-install: #устанвока пакета в пользовательское окружение
	python3 -m pip install --user dist/*.whl
