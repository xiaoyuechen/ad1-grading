#!/bin/bash
python rangen_py3x.py 100
python sort.py
sort -n nums.txt > nums_ref.txt
echo "Checking output of bubblesort"
diff bubblesorted.txt nums_ref.txt
if [ $? -eq 0 ] 
then
  echo "Ok"
else
  echo "Not ok"
fi

echo "Checking output of insertionsort"
diff insertionsorted.txt nums_ref.txt
if [ $? -eq 0 ] 
then
  echo "Ok"
else
  echo "Not ok"
fi

echo "Checking output of heapsort"
diff heapsorted.txt nums_ref.txt
if [ $? -eq 0 ] 
then
  echo "Ok"
else
  echo "Not ok"
fi

echo "Checking output of quicksort"
diff quicksorted.txt nums_ref.txt
if [ $? -eq 0 ] 
then
  echo "Ok"
else
  echo "Not ok"
fi

