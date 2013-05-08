#########	Script which Runs Linear SVM for the given input, class files and chosen features 	################
#########  	NOTE : This script needs to be modified depending on the features needed to be merged	################


test_or_train_option=$1			####	ARG 1 : '-t' for train and '-T' for Test set
class_option=$2				####	ARG 2 : -x default. Runs multi class classifier
					####	'1' - Happy vs Rest Classifier		'2' - Sad vs Rest Classifier ..... '8' - Disgust vs Rest 
language_option=$3			####	ARG 3 : 'en' for 'English', 'es' for Spanish

if [ "$4" == "-x" ]; then
	data_path='data/'		####	ARG 4 : 'Specifies the path of the data folder'
else
	data_path=$4
fi
					####	NOTE : Train and test should be run consecutively. Train followed by test always.
					####	NOTE : Feature combinations need to be modified in the argument list of 'mergeFeauresScript'
					
modelPath=$data_path'models/'
script_path='scripts/'
SVM_PATH='scripts/svm_multiclass_linux/'
noOfClasses=2

inputFileStep6=$data_path'input_step6'$test_or_train_option'.txt'
inputFileStep7=$data_path'input_step7'$test_or_train_option'.txt'
inputFileStep8=$data_path'input_step8'$test_or_train_option'.txt'


mergeFeaturesScript=$script_path'step7_MergeFeatures.py'
evaluationScript=$script_path'evaluation.py'
classFileName=""
if [ "$class_option" == "-x" ]; then
	classFileName=$data_path'classFileName'$test_or_train_option'_f.txt'
	svmModelFileName=$modelPath'SVMModel'$test_or_train_option'_f.txt'
	noOfClasses=8
else
	classFileName=$data_path'classFileName'$test_or_train_option'_f.txt'$class_option
	svmModelFileName=$modelPath'SVMModel'$test_or_train_option'_f.txt'$class_option
fi
svmInputFileName=$data_path'svmInput'$test_or_train_option'.txt'
#svmModelFileName=$data_path'svmModel.txt'
svmPredFileName=$data_path'svmPred'$test_or_train_option'.txt'

unigramFeatureFileName=$data_path'step6_UnigramFeatureOutput'$test_or_train_option'.txt'
bigramFeatureFileName=$data_path'step6_BigramFeatureOutput'$test_or_train_option'.txt'
trigramFeatureFileName=$data_path'step6_TrigramFeatureOutput'$test_or_train_option'.txt'
emoticonFeaturesFileName=$data_path'step6_EmoticonFeatureValues'$test_or_train_option'.txt'
indPolarityFileName=$data_path'step6_PolInd'$test_or_train_option'.txt' 
posNegPolarityFileName=$data_path'step6_PolPosNeg'$test_or_train_option'.txt'
totalPolarityFileName=$data_path'step6_PolTotal'$test_or_train_option'.txt'

if [ "$language_option" == "en" ]; then
	python $mergeFeaturesScript $classFileName $svmInputFileName $unigramFeatureFileName $bigramFeatureFileName $trigramFeatureFileName $emoticonFeaturesFileName $indPolarityFileName $posNegPolarityFileName $totalPolarityFileName
else
	python $mergeFeaturesScript $classFileName $svmInputFileName $unigramFeatureFileName $bigramFeatureFileName $trigramFeatureFileName $emoticonFeaturesFileName
fi

if [ "$test_or_train_option" == "-t" ]; then
	./$SVM_PATH'svm_multiclass_learn' -c 1.0 $svmInputFileName $svmModelFileName
fi

./$SVM_PATH'svm_multiclass_classify' $svmInputFileName $svmModelFileName $svmPredFileName

python $evaluationScript $svmPredFileName $classFileName $noOfClasses

