#!/bin/sh
echo "------------------------"
echo "-- POSTGRES -INI- --"
echo "------------------------"
cd /
./wait-for-it.sh db:5432 -t 0 -- echo "postgres is up"
echo "------------------------"
echo "-- POSTGRES -FIN- --"
echo "------------------------"

./wait-for-it.sh app:5555 -t 0
# python puzzle_queen.py -f -s
