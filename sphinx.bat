REM This script build upbge python API in upbgeBuild/bin/python_api/sphinx-out folder
REM First you have to install sphinx: pip install sphinx
REM Then put the file outside upbge sources folder
REM Rename upbgeSources and upbgeBuild according to your sources anb build folders
REM upbge has to be build in release mode before running this script
cd upbgeBuild/bin/Release
blender.exe --background --factory-startup --python ../../../upbgeSources/doc/python_api/sphinx_doc_gen.py -- --output ../python_api
cd ../python_api
sphinx-build sphinx-in sphinx-out
pause