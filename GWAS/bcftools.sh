#Add bcftools
Module spider bcftools/1.16
#path : StdEnv/2020  gcc/9.3.0 bcftools/1.16

#!/bin/bash
module add StdEnv/2020 samtools/1.16.1 
module add StdEnv/2020 gcc/9.3.0 bcftools/1.16

DATA=/home/vicou67/scratch/BVG-7003/SamGag/GBS_data/3_samfiles/bamlist
REF=/home/vicou67/scratch/BVG-7003/SamGag/refgenome/Gmax_275_v2.0.fa
OUT=variantcalling
CPU=4

mkdir results1
cd results1

exec &> samt_var.log

samtools mpileup -f $REF -b $DATA > variants.bcf

        if [ $? -ne 0 ]
                       	then
                            	printf "There is a problem at the samtools_mpileup step"
                                exit 1
                fi


bcftools call -mv variants.bcf > variants.vcf

        if [ $? -ne 0 ]
                       	then
                            	printf "There is a problem at the bcf2vcf step"
                                exit 1
                fi

