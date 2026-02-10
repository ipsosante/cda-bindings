#!/bin/bash

ans_repo_name="interop-outil-cda-testcontenucda3.0-outil-validation-documents-cda.git"

root_cda_dir="$1"
if [ -z "$root_cda_dir" ]; then
    echo "Expecting the path to the $ans_repo_name directory as argument"
    exit 1
fi

# See the "Patches" section of the README for an explanation on why each of these
# patches are needed.
for patch in ./patches/xsd/*.patch; do
    patch -p1 -d "$root_cda_dir" < "$patch"
done

root_cda_xsd=$(find "$root_cda_dir" -type f -name 'CDA_extended.xsd' | head -n1)

rm -rf ./cdabindings
uv run xsdata generate --debug --config .xsdata.xml "$root_cda_xsd"

for patch in ./patches/generated_code/*.patch; do
    patch -p1 < "$patch"
done

touch ./cdabindings/py.typed

# Restore the content of the ANS repo directory (reverse the patches)
for patch in ./patches/xsd/*.patch; do
    patch -p1 -R -d "$root_cda_dir" < "$patch"
done