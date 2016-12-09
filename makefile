.PHONY:

VERSION=$(shell head -1 VERSION)

 #  _   _                     ____        
 # | | | | _____   _____ _ __|  _ \ _   _ 
 # | |_| |/ _ \ \ / / _ \ '__| |_) | | | |
 # |  _  | (_) \ V /  __/ |  |  __/| |_| |
 # |_| |_|\___/ \_/ \___|_|  |_|    \__, |
 #                                  |___/ 

# Commands from most to least significant

all: 
	python setup.py build

# ┬─┐┌─┐┬  ┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┌┬┐┌─┐┬ ┬  ┌┬┐┌─┐┌─┐┌┬┐  ┬  ┬┌─┐┬─┐┌─┐┬┌─┐┌┐┌
# ├┬┘├┤ │  ├┤ ├─┤└─┐├┤   ├─┘├─┤ │ │  ├─┤   │ ├┤ └─┐ │   └┐┌┘├┤ ├┬┘└─┐││ ││││
# ┴└─└─┘┴─┘└─┘┴ ┴└─┘└─┘  ┴  ┴ ┴ ┴ └─┘┴ ┴   ┴ └─┘└─┘ ┴    └┘ └─┘┴└─└─┘┴└─┘┘└┘
release_test_patch: clean patch_tag commit push reg_and_upload_to_pypi clean

release_test: clean tag commit push reg_and_upload_to_pypi clean

reg_and_upload_to_pypi: register_test upload_test

patch_tag: semver_patch tag

tag: do_tag push_tags

test_install_from_pip:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	cd /tmp/ && pip install --install-option="--prefix=/tmp/" -i https://testpypi.python.org/pypi hoverpy
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python2.7/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test_local_tmp_install_python_2:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	mkdir -p /tmp/lib/python2.7/site-packages/
	cd /tmp/ && PYTHONPATH=/tmp/lib/python2.7/site-packages python setup.py install --prefix=/tmp
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python2.7/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test_local_tmp_install_python_3:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	mkdir -p /tmp/lib/python3/site-packages/
	PYTHONPATH=/tmp/lib/python3/site-packages python3 setup.py install --prefix=/tmp
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python3/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test:
	python setup.py test
	python3.6 setup.py test

docs: .PHONY
	python hoverpy/generateDocs.py

	pandoc --from=markdown --to=rst --output=docs/source/README.rst README.md

	mv examples/basic/basic.rst docs/source/
	mv examples/readthedocs/readthedocs.rst docs/source/
	mv examples/modify/modify.rst docs/source/
	mv examples/modify/modify_payload.rst docs/source/
	mv examples/delays/delays.rst docs/source/
	mv examples/unittesting/unittesting.rst docs/source/
	mv examples/urllib2eg/urllib2eg.rst docs/source/
	mv examples/urllib3eg/urllib3eg.rst docs/source/

	#sphinx-apidoc -o docs/source/ hoverpy
	
	cd docs; make html;
#	cd docs/source/mermaid/intro; mermaid *;

### -------------------------------------------------------------------------------
## You'll need to save this into your ~/.pypirc if you'd like to push this to pypi

# [distutils]
# index-servers =
#   pypi
#   pypitest

# [pypi]
# repository=https://pypi.python.org/pypi
# username=
# password=

# [pypitest]
# repository=https://testpypi.python.org/pypi
# username=
# password=

### ------------------------------------
### ------------------------------------
## Probably nothing interesting below

register_test:
	python setup.py register -r pypitest

upload_test:
	python setup.py sdist upload -r pypitest

do_tag:
	git tag $(VERSION) -m "Adds a tag so that we can put this on PyPI."

push_tags:
	git push --tags origin 

commit:
	git add .
	git commit -am "updated"

push:
	git push

semver_patch:
	semver `head -1 VERSION` -i patch > VERSION
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ setup.py
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ hoverpy/config.py
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ docs/source/conf.py
	rm -f `find . -name '*.bak'`

clean:
	rm -rf build dist hoverpy.egg-info /tmp/hover* /tmp/lib .eggs hoverpy/__pycache__
	rm -f `find . -name "hoverfly.log"`
	rm -f `find . -name "middleware.log"`
	rm -f `find . -name "*.pyc"`
	rm -rf `find . -name '__pycache__'`
	cd docs; make clean
