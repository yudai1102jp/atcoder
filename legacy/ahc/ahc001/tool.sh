#!/bin/bash
FILE=0
REC="record"
N=30
cd /Users/yudai/Desktop/atcoder/ahc001/tools
echo ${N} > ${REC}.txt

for ((i=0;i<N;i++))
do
    FILE=`printf %04d $FILE`
    
    cd /Users/yudai/Desktop/atcoder/ahc001
    
    python3.8 min.py < tools/in/${FILE}.txt > tools/out.txt
    
    cd tools
    
    cargo run --release --bin vis in/${FILE}.txt out.txt >> ${REC}.txt
    
    FILE=`expr $FILE + 1`
done
cd /Users/yudai/Desktop/atcoder/ahc001
python3.8 test.py < tools/${REC}.txt