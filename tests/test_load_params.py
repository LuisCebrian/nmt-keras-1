import unittest
from config import load_parameters


class TestLoadParams(unittest.TestCase):

    def test_load_params(self):
        params = load_parameters()
        self.assertIsInstance(params, dict)

    def test_params_exist(self):
        params = load_parameters()
        self.assertIn('DATASET_NAME', params.keys())
        self.assertIn('SRC_LAN', params.keys())
        self.assertIn('TRG_LAN', params.keys())
        self.assertIn('DATA_ROOT_PATH', params.keys())
        self.assertIn('TEXT_FILES', params.keys())
        self.assertIn('INPUTS_IDS_DATASET', params.keys())
        self.assertIn('OUTPUTS_IDS_DATASET', params.keys())
        self.assertIn('INPUTS_IDS_MODEL', params.keys())
        self.assertIn('OUTPUTS_IDS_MODEL', params.keys())
        self.assertIn('METRICS', params.keys())
        self.assertIn('EVAL_ON_SETS', params.keys())
        self.assertIn('EVAL_ON_SETS_KERAS', params.keys())
        self.assertIn('START_EVAL_ON_EPOCH', params.keys())
        self.assertIn('EVAL_EACH_EPOCHS', params.keys())
        self.assertIn('EVAL_EACH', params.keys())
        self.assertIn('SAMPLING', params.keys())
        self.assertIn('TEMPERATURE', params.keys())
        self.assertIn('BEAM_SEARCH', params.keys())
        self.assertIn('BEAM_SIZE', params.keys())
        self.assertIn('OPTIMIZED_SEARCH', params.keys())
        self.assertIn('LENGTH_PENALTY', params.keys())
        self.assertIn('LENGTH_NORM_FACTOR', params.keys())
        self.assertIn('COVERAGE_PENALTY', params.keys())
        self.assertIn('COVERAGE_NORM_FACTOR', params.keys())
        self.assertIn('NORMALIZE_SAMPLING', params.keys())
        self.assertIn('ALPHA_FACTOR', params.keys())
        self.assertIn('SAMPLE_ON_SETS', params.keys())
        self.assertIn('N_SAMPLES', params.keys())
        self.assertIn('START_SAMPLING_ON_EPOCH', params.keys())
        self.assertIn('SAMPLE_EACH_UPDATES', params.keys())
        self.assertIn('POS_UNK', params.keys())
        self.assertIn('HEURISTIC', params.keys())
        self.assertIn('ALIGN_FROM_RAW', params.keys())
        self.assertIn('MAPPING', params.keys())
        self.assertIn('TOKENIZATION_METHOD', params.keys())
        self.assertIn('DETOKENIZATION_METHOD', params.keys())
        self.assertIn('APPLY_DETOKENIZATION', params.keys())
        self.assertIn('TOKENIZE_HYPOTHESES', params.keys())
        self.assertIn('TOKENIZE_REFERENCES', params.keys())
        self.assertIn('DATA_AUGMENTATION', params.keys())
        self.assertIn('FILL', params.keys())
        self.assertIn('PAD_ON_BATCH', params.keys())
        self.assertIn('INPUT_VOCABULARY_SIZE', params.keys())
        self.assertIn('MIN_OCCURRENCES_INPUT_VOCAB', params.keys())
        self.assertIn('MAX_INPUT_TEXT_LEN', params.keys())
        self.assertIn('OUTPUT_VOCABULARY_SIZE', params.keys())
        self.assertIn('MIN_OCCURRENCES_OUTPUT_VOCAB', params.keys())
        self.assertIn('MAX_OUTPUT_TEXT_LEN', params.keys())
        self.assertIn('MAX_OUTPUT_TEXT_LEN_TEST', params.keys())
        self.assertIn('LOSS', params.keys())
        self.assertIn('CLASSIFIER_ACTIVATION', params.keys())
        self.assertIn('OPTIMIZER', params.keys())
        self.assertIn('LR', params.keys())
        self.assertIn('CLIP_C', params.keys())
        self.assertIn('CLIP_V', params.keys())
        self.assertIn('SAMPLE_WEIGHTS', params.keys())
        self.assertIn('LR_DECAY', params.keys())
        self.assertIn('LR_GAMMA', params.keys())
        self.assertIn('MAX_EPOCH', params.keys())
        self.assertIn('BATCH_SIZE', params.keys())
        self.assertIn('HOMOGENEOUS_BATCHES', params.keys())
        self.assertIn('JOINT_BATCHES', params.keys())
        self.assertIn('PARALLEL_LOADERS', params.keys())
        self.assertIn('EPOCHS_FOR_SAVE', params.keys())
        self.assertIn('WRITE_VALID_SAMPLES', params.keys())
        self.assertIn('SAVE_EACH_EVALUATION', params.keys())
        self.assertIn('EARLY_STOP', params.keys())
        self.assertIn('PATIENCE', params.keys())
        self.assertIn('STOP_METRIC', params.keys())
        self.assertIn('MODEL_TYPE', params.keys())
        self.assertIn('RNN_TYPE', params.keys())
        self.assertIn('INIT_FUNCTION', params.keys())
        self.assertIn('SOURCE_TEXT_EMBEDDING_SIZE', params.keys())
        self.assertIn('SRC_PRETRAINED_VECTORS', params.keys())
        self.assertIn('SRC_PRETRAINED_VECTORS_TRAINABLE', params.keys())
        self.assertIn('TARGET_TEXT_EMBEDDING_SIZE', params.keys())
        self.assertIn('TRG_PRETRAINED_VECTORS', params.keys())
        self.assertIn('TRG_PRETRAINED_VECTORS_TRAINABLE', params.keys())
        self.assertIn('ENCODER_HIDDEN_SIZE', params.keys())
        self.assertIn('BIDIRECTIONAL_ENCODER', params.keys())
        self.assertIn('N_LAYERS_ENCODER', params.keys())
        self.assertIn('BIDIRECTIONAL_DEEP_ENCODER', params.keys())
        self.assertIn('DECODER_HIDDEN_SIZE', params.keys())
        self.assertIn('N_LAYERS_DECODER', params.keys())
        self.assertIn('ADDITIONAL_OUTPUT_MERGE_MODE', params.keys())
        self.assertIn('ATTENTION_SIZE', params.keys())
        self.assertIn('SKIP_VECTORS_HIDDEN_SIZE', params.keys())
        self.assertIn('INIT_LAYERS', params.keys())
        self.assertIn('DEEP_OUTPUT_LAYERS', params.keys())
        self.assertIn('WEIGHT_DECAY', params.keys())
        self.assertIn('RECURRENT_WEIGHT_DECAY', params.keys())
        self.assertIn('USE_DROPOUT', params.keys())
        self.assertIn('DROPOUT_P', params.keys())
        self.assertIn('USE_RECURRENT_INPUT_DROPOUT', params.keys())
        self.assertIn('RECURRENT_INPUT_DROPOUT_P', params.keys())
        self.assertIn('USE_RECURRENT_DROPOUT', params.keys())
        self.assertIn('RECURRENT_DROPOUT_P', params.keys())
        self.assertIn('USE_NOISE', params.keys())
        self.assertIn('NOISE_AMOUNT', params.keys())
        self.assertIn('USE_BATCH_NORMALIZATION', params.keys())
        self.assertIn('BATCH_NORMALIZATION_MODE', params.keys())
        self.assertIn('USE_PRELU', params.keys())
        self.assertIn('USE_L2', params.keys())
        self.assertIn('EXTRA_NAME', params.keys())
        self.assertIn('MODEL_NAME', params.keys())
        self.assertIn('STORE_PATH', params.keys())
        self.assertIn('DATASET_STORE_PATH', params.keys())
        self.assertIn('SAMPLING_SAVE_MODE', params.keys())
        self.assertIn('VERBOSE', params.keys())
        self.assertIn('RELOAD', params.keys())
        self.assertIn('RELOAD_EPOCH', params.keys())
        self.assertIn('REBUILD_DATASET', params.keys())
        self.assertIn('MODE', params.keys())
        self.assertIn('TRAIN_ON_TRAINVAL', params.keys())
        self.assertIn('FORCE_RELOAD_VOCABULARY', params.keys())

    def test_params_type(self):
        params = load_parameters()
        self.assertIsInstance(params['DATASET_NAME'], str)
        self.assertIsInstance(params['SRC_LAN'], str)
        self.assertIsInstance(params['TRG_LAN'], str)
        self.assertIsInstance(params['DATA_ROOT_PATH'], str)
        self.assertIsInstance(params['TEXT_FILES'], dict)
        self.assertIsInstance(params['INPUTS_IDS_DATASET'], list)
        self.assertIsInstance(params['OUTPUTS_IDS_DATASET'], list)
        self.assertIsInstance(params['INPUTS_IDS_MODEL'], list)
        self.assertIsInstance(params['OUTPUTS_IDS_MODEL'], list)
        self.assertIsInstance(params['METRICS'], list)
        self.assertIsInstance(params['EVAL_ON_SETS'], list)
        self.assertIsInstance(params['EVAL_ON_SETS_KERAS'], list)
        self.assertIsInstance(params['START_EVAL_ON_EPOCH'], int)
        self.assertIsInstance(params['EVAL_EACH_EPOCHS'], bool)
        self.assertIsInstance(params['EVAL_EACH'], int)
        self.assertIsInstance(params['SAMPLING'], str)
        self.assertIsInstance(params['TEMPERATURE'], int)
        self.assertIsInstance(params['BEAM_SEARCH'], bool)
        self.assertIsInstance(params['BEAM_SIZE'], int)
        self.assertIsInstance(params['OPTIMIZED_SEARCH'], bool)
        self.assertIsInstance(params['LENGTH_PENALTY'], bool)
        self.assertIsInstance(params['LENGTH_NORM_FACTOR'], float)
        self.assertIsInstance(params['COVERAGE_PENALTY'], bool)
        self.assertIsInstance(params['COVERAGE_NORM_FACTOR'], float)
        self.assertIsInstance(params['NORMALIZE_SAMPLING'], bool)
        self.assertIsInstance(params['ALPHA_FACTOR'], float)
        self.assertIsInstance(params['SAMPLE_ON_SETS'], list)
        self.assertIsInstance(params['N_SAMPLES'], int)
        self.assertIsInstance(params['START_SAMPLING_ON_EPOCH'], int)
        self.assertIsInstance(params['SAMPLE_EACH_UPDATES'], int)
        self.assertIsInstance(params['POS_UNK'], bool)
        self.assertIsInstance(params['HEURISTIC'], int)
        self.assertIsInstance(params['ALIGN_FROM_RAW'], bool)
        self.assertIsInstance(params['MAPPING'], str)
        self.assertIsInstance(params['TOKENIZATION_METHOD'], str)
        self.assertIsInstance(params['DETOKENIZATION_METHOD'], str)
        self.assertIsInstance(params['APPLY_DETOKENIZATION'], bool)
        self.assertIsInstance(params['TOKENIZE_HYPOTHESES'], bool)
        self.assertIsInstance(params['TOKENIZE_REFERENCES'], bool)
        self.assertIsInstance(params['DATA_AUGMENTATION'], bool)
        self.assertIsInstance(params['FILL'], str)
        self.assertIsInstance(params['PAD_ON_BATCH'], bool)
        self.assertIsInstance(params['INPUT_VOCABULARY_SIZE'], int)
        self.assertIsInstance(params['MIN_OCCURRENCES_INPUT_VOCAB'], int)
        self.assertIsInstance(params['MAX_INPUT_TEXT_LEN'], int)
        self.assertIsInstance(params['OUTPUT_VOCABULARY_SIZE'], int)
        self.assertIsInstance(params['MIN_OCCURRENCES_OUTPUT_VOCAB'], int)
        self.assertIsInstance(params['MAX_OUTPUT_TEXT_LEN'], int)
        self.assertIsInstance(params['MAX_OUTPUT_TEXT_LEN_TEST'], int)
        self.assertIsInstance(params['LOSS'], str)
        self.assertIsInstance(params['CLASSIFIER_ACTIVATION'], str)
        self.assertIsInstance(params['OPTIMIZER'], str)
        self.assertIsInstance(params['LR'], float)
        self.assertIsInstance(params['CLIP_C'], float)
        self.assertIsInstance(params['CLIP_V'], float)
        self.assertIsInstance(params['SAMPLE_WEIGHTS'], bool)
        self.assertIs(params['LR_DECAY'], None)
        self.assertIsInstance(params['LR_GAMMA'], float)
        self.assertIsInstance(params['MAX_EPOCH'], int)
        self.assertIsInstance(params['BATCH_SIZE'], int)
        self.assertIsInstance(params['HOMOGENEOUS_BATCHES'], bool)
        self.assertIsInstance(params['JOINT_BATCHES'], int)
        self.assertIsInstance(params['PARALLEL_LOADERS'], int)
        self.assertIsInstance(params['EPOCHS_FOR_SAVE'], int)
        self.assertIsInstance(params['WRITE_VALID_SAMPLES'], bool)
        self.assertIsInstance(params['SAVE_EACH_EVALUATION'], bool)
        self.assertIsInstance(params['EARLY_STOP'], bool)
        self.assertIsInstance(params['PATIENCE'], int)
        self.assertIsInstance(params['STOP_METRIC'], str)
        self.assertIsInstance(params['MODEL_TYPE'], str)
        self.assertIsInstance(params['RNN_TYPE'], str)
        self.assertIsInstance(params['INIT_FUNCTION'], str)
        self.assertIsInstance(params['SOURCE_TEXT_EMBEDDING_SIZE'], int)
        self.assertIs(params['SRC_PRETRAINED_VECTORS'], None)
        self.assertIsInstance(params['SRC_PRETRAINED_VECTORS_TRAINABLE'], bool)
        self.assertIsInstance(params['TARGET_TEXT_EMBEDDING_SIZE'], int)
        self.assertIs(params['TRG_PRETRAINED_VECTORS'], None)
        self.assertIsInstance(params['ENCODER_HIDDEN_SIZE'], int)
        self.assertIsInstance(params['BIDIRECTIONAL_ENCODER'], bool)
        self.assertIsInstance(params['N_LAYERS_ENCODER'], int)
        self.assertIsInstance(params['BIDIRECTIONAL_DEEP_ENCODER'], bool)
        self.assertIsInstance(params['DECODER_HIDDEN_SIZE'], int)
        self.assertIsInstance(params['N_LAYERS_DECODER'], int)
        self.assertIsInstance(params['ATTENTION_SIZE'], int)
        self.assertIsInstance(params['ADDITIONAL_OUTPUT_MERGE_MODE'], str)
        self.assertIsInstance(params['SKIP_VECTORS_HIDDEN_SIZE'], int)
        self.assertIsInstance(params['INIT_LAYERS'], list)
        self.assertIsInstance(params['DEEP_OUTPUT_LAYERS'], list)
        self.assertIsInstance(params['WEIGHT_DECAY'], float)
        self.assertIsInstance(params['RECURRENT_WEIGHT_DECAY'], float)
        self.assertIsInstance(params['USE_DROPOUT'], bool)
        self.assertIsInstance(params['DROPOUT_P'], float)
        self.assertIsInstance(params['USE_RECURRENT_INPUT_DROPOUT'], bool)
        self.assertIsInstance(params['RECURRENT_INPUT_DROPOUT_P'], float)
        self.assertIsInstance(params['USE_RECURRENT_DROPOUT'], bool)
        self.assertIsInstance(params['RECURRENT_DROPOUT_P'], float)
        self.assertIsInstance(params['USE_NOISE'], bool)
        self.assertIsInstance(params['NOISE_AMOUNT'], float)
        self.assertIsInstance(params['USE_BATCH_NORMALIZATION'], bool)
        self.assertIsInstance(params['BATCH_NORMALIZATION_MODE'], int)
        self.assertIsInstance(params['USE_PRELU'], bool)
        self.assertIsInstance(params['USE_L2'], bool)
        self.assertIsInstance(params['EXTRA_NAME'], str)
        self.assertIsInstance(params['MODEL_NAME'], str)
        self.assertIsInstance(params['STORE_PATH'], str)
        self.assertIsInstance(params['DATASET_STORE_PATH'], str)
        self.assertIsInstance(params['SAMPLING_SAVE_MODE'], str)
        self.assertIsInstance(params['VERBOSE'], int)
        self.assertIsInstance(params['RELOAD'], int)
        self.assertIsInstance(params['RELOAD_EPOCH'], bool)
        self.assertIsInstance(params['REBUILD_DATASET'], bool)
        self.assertIsInstance(params['MODE'], str)
        self.assertIsInstance(params['TRAIN_ON_TRAINVAL'], bool)
        self.assertIsInstance(params['FORCE_RELOAD_VOCABULARY'], bool)

if __name__ == '__main__':
    unittest.main()
