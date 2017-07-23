rm temp
for i in `seq 1 10`
do	
	printf "cp color/*class%02d* ./class_%02d\n" $i $i >> temp
done

for j in `seq 1 18`
do
        printf "cp depth/*class%02d* ./class_%02d\n" $j $j >> temp
done

sh temp
rm temp

