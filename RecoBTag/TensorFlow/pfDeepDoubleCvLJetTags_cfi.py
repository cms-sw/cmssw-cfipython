import FWCore.ParameterSet.Config as cms

pfDeepDoubleCvLJetTags = cms.EDProducer('DeepDoubleXTFJetTagsProducer',
  src = cms.InputTag('pfDeepDoubleXTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3'
  ),
  lp_names = cms.vstring('db_input_batchnorm/keras_learning_phase'),
  output_names = cms.vstring('ID_pred/Softmax'),
  batch_eval = cms.bool(False),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads'),
  flavor = cms.string('CvL'),
  flav_table = cms.PSet(
    probQCD = cms.vuint32(0),
    probHcc = cms.vuint32(1)
  ),
  graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleX/94X/V01/DDC.pb')
)
