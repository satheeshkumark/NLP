corpus_option=$1     ############################### 'PNS' or 'SNS'
classifier_option=$2 ############################### '-bi' or '-tri'

data_path='data/'
script_path='scripts/'
SVM_path='scripts/svm_multiclass_linux/'
SVM_Model_File=$data_path$corpus_option$classifier_option'_SVM.model'
evaluation_Script=$script_path'evaluation.py'

SVM_TrainFilename=$data_path'SVMInput_'$corpus_option$classifier_option'-t.txt'
SVM_TestFilename=$data_path'SVMInput_'$corpus_option$classifier_option'-T.txt'
SVM_PredTrainFilename=$data_path'SVMPred_'$corpus_option$classifier_option'-t.txt'
SVM_PredTestFilename=$data_path'SVMPred_'$corpus_option$classifier_option'-T.txt'

SVM_TrainClassFilename=$data_path'step2_'$corpus_option'InputCorpus'$classifier_option'-t-class.txt'
SVM_TestClassFilename=$data_path'step2_'$corpus_option'InputCorpus'$classifier_option'-T-class.txt'
#SVM_TestClassFilename=$data_path'fbclass.txt'

noOfClasses=2
noOfAccuracyClasses=2
noOfTrainExamples=10000
noOfTestExamples=2000

if [ "$corpus_option" == "PNS" ]; then
	if [ "$classifier_option" == "-tri" ]; then
		noOfClasses=3
		noOfAccuracyClasses=3
		noOfTrainExamples=15000
		noOfTestExamples=3000
	elif [ "$classifier_option" == "-bi" ]; then
		noOfClasses=2
		noOfAccuracyClasses=2
		noOfTrainExamples=15000
		noOfTestExamples=3000
	fi
fi

#noOfClasses=2
#noOfAccuracyClasses=2
#noOfTrainExamples=15000
#noOfTestExamples=368

####################################### Generating the model #############################################################################

./$SVM_path'svm_multiclass_learn' -c 1.0 $SVM_TrainFilename $SVM_Model_File  


####################################### Applying the model on train data ##################################################################

./$SVM_path'svm_multiclass_classify' $SVM_TrainFilename $SVM_Model_File $SVM_PredTrainFilename

python $evaluation_Script $SVM_PredTrainFilename $SVM_TrainClassFilename $noOfClasses $noOfTrainExamples $noOfAccuracyClasses


echo 'SVM_PredTrainFilename : '$SVM_PredTrainFilename
#echo 'SVM Model File name : '$SVM_TrainClassFilename
echo 'SVM Pred Train Class File Name : '$SVM_TrainClassFilename
echo 'Number of classes : '$noOfClasses
echo 'Number of Train examples : '$noOfTrainExamples
echo 'Accuracy class : '$noOfAccuracyClasses
echo
echo

####################################### Applying the model on train data ##################################################################

./$SVM_path'svm_multiclass_classify' $SVM_TestFilename $SVM_Model_File $SVM_PredTestFilename

python $evaluation_Script $SVM_PredTestFilename $SVM_TestClassFilename $noOfClasses $noOfTestExamples $noOfAccuracyClasses

