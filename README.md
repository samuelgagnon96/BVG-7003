# BVG-7003
This document was produced during my BVG-7003 class at Laval University. This class is about bioinformatic tools and how to properly use them in our own study. 

## PythonBiopython
The first project concerned Python and BioPython. 
You can find the scripts for this project of the PythonBiopython file on my Github.
For this project, we had to write coding lines based on our notes on the basic functions of Python and Biopython. The file Python.py shows the python scripts and Biopython.py file shows the biopython scripts.
This guide could be useful for all new programmer who wants to learn the basics of Python and Biopython.

We used Pycharm to write and run the scripts, so the first step is to download Pycharm on your computer. Here's the link for the free version of Pycharm: https://www.jetbrains.com/pycharm/download/#section=mac

Once you have Pycharm Downloaded, make sure that you are running the lateast version or Python on your Pycharm. The latest version when i ran my scritps was 3.10.

To Run the Biopython scripts, you'll have to install some packages in Pycharm. Those are the packages you'll need for this project: numpy, biopython, matplolib and pylablib.


The second project was about GWAS and how to use the tools to work with the genotypic data. This project is divided in many smaller scripts that represent every step of the process. 
This project was run on the NARVAL server explaining why some lines in the scripts explain how to install the different tools in this new environment. 

The sabre.sh file includes the scripts to sort the sequences accroding to their barcodes. This script uses the tool sabre.

The cutadapt.sh file regroup all the scripts that are necessary to cut the adapters from the sequences. The files at the end of this process are fastq files. This script uses the tool cutadapt.

The bwa.sh file includes the scripts to convert the fastq to sam files. This script uses the bwa tool. 

The sam2bam.sh file explains the scripts to convert the sam files into bam files and it uses the samtools tool. 

The final file, bcftools.sh, takes the bam files and makes the variant calls. This step uses bcftools. 


All the scripts are working, the only issue if you want to run them is that you'll need to change the various trajectories to your own on your computer. 

If you have any issues or questions about this scripts or those tools you can join me by email on: samuel.gagnon.19@ulaval.ca

Have a nice programming session. 



README file R Studio

This third project involves R Studio. 
For this you will need to install R Studio on your computer. Here’s the link to install this platform: https://posit.co/download/rstudio-desktop/



Wang J., Zhang Z., GAPIT Version 3: Boosting Power and Accuracy for Genomic Association and Prediction, Genomics, Proteomics & Bioinformatics (2021), doi: https://doi.org/10.1016/j.gpb.2021.08.005.

The first step is to install the packages in the R Studio Library.
