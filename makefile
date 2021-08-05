install:
	pip3 install .
publish:
	python3 -m build
	twine upload dist/*
	pip3 install --upgrade smidge
