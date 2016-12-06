#!/bin/bash

#$ -N forward_selection
#$ -M kag29@njit.edu
#$ -m ae
#$ -cwd 
#$ -j y
#$ -q short

module load python2
module load R-Project

COUNTER=0

for COUNTER in {0..9}
do
    echo "working on file ${COUNTER}"
    FILE="../training_labels/split.70.30.training.${COUNTER}"
    OUTFILE="svm.all.${COUNTER}"
    python svm.py ${HOME}/cs675_project/traindata $FILE ${OUTFILE}.out
    python be.py ${FILE}.out.predict ../../project/trueclass >> error
done

python average_error.py error >> avg_error

for i in {0..29623}
do
    python svm_col.py ${HOME}/cs675_project/traindata \
    "../training_labels/split.70.30.training.4" col.${i}.out $i
    python be_col.py col.${i}.out.predict ${HOME}/cs675_project/trueclass $i >> col_error
done
