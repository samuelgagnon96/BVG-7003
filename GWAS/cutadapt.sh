#Remove the adapters

#create an environment with python 
module load python/3.10 scipy-stack/2022a 

#initialize virtual environment
virtualenv --no-download /home/vicou67/scratch/BVG-7003/SamGag/GBS_data\

 #activate virtual environment
source /home/vicou67/scratch/BVG-7003/SamGag/GBS_data/bin/activate

#upgrade pip and install cutadapt 
pip install --no-index --upgrade pip python3 -m pip install –vicou67 --upgrade cutadapt 

#Out of virtual environment 
deactivate

#Remove adapters 
#!/bin/bash
cd NGS
ADAP=AGATCGGAA
exec &> cutadapt.log
parallel -j 4 cutadapt -a $ADAP -m 50 -o {}.fastq {}.fq ::: $(ls -1 *.fq | sed 's/.fq//')
	if [ $? -ne 0 ]
		then
			printf There is error in the cutadapt
			exit 1
	fi
