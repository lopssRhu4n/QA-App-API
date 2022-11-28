.PHONY: install format lint test

run-env:
	@poetry shell

run-dev: 
	@flask --app src/app.py --debug run

install: 
	@poetry install
	
format: 
	@blue .

lint: 
	@blue  . --check
	@prospector 

test:
	@pytest -v

clear:
	@pyclean -v
