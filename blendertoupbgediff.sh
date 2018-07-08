dir=$(pwd)
echo $dir
cd $1

git diff blender/master master -- . \
":!source/gameengine/" \
":!intern/container/" \
":!intern/moto/" \
":!.gitmodules" \
":!README.md" \
":!source/blender/windowmanager/intern/wm_operators.c" \
":!doc/python_api/rst/bge.app.rst" \
":!source/blender/blenkernel/BKE_blender_version.h" \
":!source/blender/blenkernel/BKE_main.h" \
":!source/blender/blenloader/intern/versioning_upbge.c" \
":!source/blender/makesdna/DNA_fileglobal_types.h" \
":!release/datafiles/" \
":!doc/python_api/" \
> ${dir}/blendertoupbge.diff

# filterdiff -p 1 \
# -x .gitmodules \
# -x README.md \
# -x source/blender/windowmanager/intern/wm_operators.c \
# -x "intern/container/*" \
# -x "source/gameengine/*" \
