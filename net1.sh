#!/bin/sh

site='www.google.com'
until $(ping -q -c1 ${site} > /dev/null 2>&1)
do
    echo "${site} is unreachable. Retrying(1)"
sleep  15s
./net2.sh
    # continue
done

echo "online"
sleep 300s
./net.sh
