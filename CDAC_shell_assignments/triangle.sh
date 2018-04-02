#!/bin/bash 
read s1 s2 s3
if [ $s1 -eq $s2 -a $s2 -eq $s3]:
then
echo "Equilateral"
elif [ $s1 -eq $s2 -o $s1 -eq $s3 -o $s2 -eq $s3]
then 
echo "Isosceles"
else
echo "Scalene"
fi

	
	
