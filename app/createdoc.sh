#!/bin/bash
rm -rf ../doc
mkdir ../doc
for module in Model Views Controller Utilities; do
	for file in $module/*.py; do
		pydoc3 -w $module.$(basename "${file%.*}")
	done
done
mv *.html ../doc




