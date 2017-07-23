rm temp
for i in `seq 1 10`
do
	printf "mkdir -p class_%02d\n" $i >> temp
done
sh temp
rm temp
