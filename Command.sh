#!/bin/bash

# Declare the a, b, c Find the greater number among them.
a=10
b=5
c=20

echo "Let's find the greatest number!"
echo "a = $a, b = $b, c = $c"

if [[ $a -gt $b && $a -gt $c ]]
then
    echo "A = $a is greater"
elif [[ $b -gt $a && $b -gt $c ]]
then
    echo "B = $b is greater"
else
    echo "C = $c is greater"
fi