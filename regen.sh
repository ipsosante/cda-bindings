#!/bin/bash

root_cda_dir="$1"
if [ -z "$root_cda_dir" ]; then
    echo "Expecting the path to the TestContenuCDA directory as argument"
    exit 1
fi

if ! type -a xsdata >/dev/null 2>&1; then
    echo "Unknown command: xsdata"
    echo "Have you activated your virtualenv and installed the required dependencies?"
    exit 2
fi

# See the "Patches" section of the README for an explanation on why each of these
# patches are needed.
for patch in ./*.patch; do
    patch -p1 -d "$root_cda_dir" < "$patch"
done

root_cda_xsd=$(find "$root_cda_dir" -type f -name 'CDA_extended.xsd' | head -n1)

rm -rf ./cdabindings
xsdata generate --debug --config .xsdata.xml "$root_cda_xsd"

# Restore the content of the TestContenuCDA directory
for patch in ./*.patch; do
    patch -p1 -R -d "$root_cda_dir" < "$patch"
done