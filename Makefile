init:
	python3.10 -m venv .venv
	source .venv/bin/source && pip install requirements.txt

clean: 
	rm -rf .venv
	rm -rf __pycache__

test:
	python testPoly.py

run:
	python examples/example_bobalice.py
	python examples/example_enDom.py
