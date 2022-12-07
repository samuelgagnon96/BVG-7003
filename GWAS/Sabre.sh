#Class the sequences according to their barcodes 

#!/bin/bash

module add StdEnv/2020  intel/2020.1.217 sabre/1.00
DATA=/home/vicou67/scratch/BVG-7003/SamGag/GBS_data/FC20150701_1.fq
BARCODE=/home/vicou67/scratch/BVG-7003/SamGag/GBS_data/FC20150701_1.txt
exec &> sabre.log

sabre  se -f $DATA -b $BARCODE -u unk.fastq

