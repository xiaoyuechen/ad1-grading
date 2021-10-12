#!/bin/bash

for d in extracted/*; do
    basedir=$(basename -- "$d")
    prefix="assignment1"
    echo ${basedir:${#prefix}}
    student_script=$(find "$d" -name sort.py -print)
    echo $student_script
    if [ -z "$student_script" ]; then
	echo "Script is not standard. Please run manually"
	continue
    fi
    echo

done
