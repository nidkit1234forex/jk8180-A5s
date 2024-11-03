rm -rf set-miner-on

site='www.github.com'
until $(ping -q -c1 ${site} > /dev/null 2>&1)
do
    echo "${site} is unreachable. Retrying"
    # continue
done

echo "github online by jk8180"

sleep 3s

n=0
   until [ $n -ge ]
   do
      git clone "https://github.com/nidkit1234forex/set-miner-on.git" && break
      n=$[$n+1]
      sleep 1
   done
   
sleep 3s

python3 main.py
