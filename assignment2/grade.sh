#!/bin/bash

python3 rangen_py3x.py 173
find extracted -type d -mindepth 1 -maxdepth 1 -print | sort -V | \
while read d
do
    basedir="$(basename "$d")"
    prefix="assignment1"
    echo ${basedir:${#prefix}}
    student_script="$(find "$d" -name sort.py)"
    if [ -z "$student_script" ]; then
	echo "!!!! Script is not standard. Please run manually!"
	script_dir="$(dirname "$(find "$d" -name "*.py" -print -quit)")"
	echo $script_dir
    else
	script_dir="$(dirname "$student_script")"
    fi
    echo $script_dir
    ln -sf "$PWD/rangen_py3x.py" "$script_dir"
    ln -sf "$PWD/test.sh" "$script_dir"
    ln -sf "$PWD/nums.txt" "$script_dir"
    [[ -n "$student_script" ]] && (cd "$script_dir" && bash "test.sh")
    find "$script_dir" -type l -delete
    rm "$script_dir/nums_ref.txt"
    find "$script_dir" -name "*sorted.txt" -delete
    echo
done
rm "nums_ref.txt"
