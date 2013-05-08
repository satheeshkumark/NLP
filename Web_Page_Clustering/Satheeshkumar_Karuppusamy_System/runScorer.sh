SCORER_PATH='../scorer_1.1/'
KEYS_DIR_PATH='../Satheeshkumar_Karuppusamy_CL/KeysDir/'
SYS_DIR_PATH='../Satheeshkumar_Karuppusamy_CL/SystemsDir/'
OUT_DIR_PATH='../Satheeshkumar_Karuppusamy_Score/'


################################################### Runs the scorer and compares the gold .xml file with all other .xml files


java -cp $SCORER_PATH'wepsEvaluation.jar' 'es.nlp.uned.weps.evaluation.SystemScorer' $KEYS_DIR_PATH $SYS_DIR_PATH $OUT_DIR_PATH -ALLMEASURES -AllInOne -OneInOne -Combined -average
