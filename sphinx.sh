#$1: program
#$2: blender directory

cd $2
$1 --background --factory-startup -noaudio --python doc/python_api/sphinx_doc_gen.py
sphinx-build -j 8 doc/python_api/sphinx-in doc/python_api/sphinx-out
