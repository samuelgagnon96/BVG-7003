#install bwa
StdEnv/2020 bwa/0.7.17

#Convert Fastq files into sam file
#!/bin/bash
module add StdEnv/2020 bwa/0.7.17
DATA=/home/vicou67/scratch/BVG-7003/SamGag/GBS_data/2_cutadapt
REF=/home/vicou67/scratch/BVG-7003/SamGag/refgenome/Gmax_275_v2.0.fa
CPU=3
THR=2
exec &> bwa.log
cd $DATA
                parallel -j $CPU bwa mem -t $THR $REF {}.fastq ">" {}.sam ::: $(ls -1 *.fastq | sed 's/.fastq//>
                if [ $? -ne 0 ]
                        then 
                             	printf There is a problem in the alignment step
                                exit 1
                fi

