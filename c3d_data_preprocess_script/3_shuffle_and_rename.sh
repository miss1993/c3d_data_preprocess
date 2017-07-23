#!/usr/bin/bash  
rm kkk
echo "----------------------------------------"
#function to create a random number  
function rand(){  
    min=$1  
    max=$(($2-$min+1))  
    num=$(date +%s%N)  
    echo $(($num%$max+$min))  
}  
echo "-------------------START--------------------"
#compute the avi-number in one class_dir

for file in ./*
do
avi_num=0
	for avi in $file/*".avi"
	do
	avi_num=`expr $avi_num + 1`
	done	
echo "Shuffle $file ......"
#create the random series for each class_dir
ar[0]=0
for i in `seq 1 $avi_num`
do
	while [ 1 ]
	do	
		rnd=$(rand 1 $avi_num)
 		num=$rnd
		ar[$i]=$num
		flag_add=0
		for j in `seq 1 $i`
		do	
			if [ $num -ne ${ar[$j]} ];then
				flag_add=`expr $flag_add + 1`
			fi
		done
		if [ $flag_add -eq `expr $i - 1` ];then	
			break
		else 
			continue
		fi
	done
done
i=0
	for avi in $file/*".avi"
	do	i=`expr $i+1`
        printf "mv %s %s/subject_%02d.avi \n" $avi $file ${ar[$i]} >> kkk
	done
echo "Done!"
done
sh kkk
rm kkk
echo Done!
	



#exit 0  
