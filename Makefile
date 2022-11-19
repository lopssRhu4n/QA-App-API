.PHONY: install format lint test

install: 
	@poetry install

format: 
	@blue .

lint: 
	@blue  . --check
	@prospector 

test:
	@pytest -v