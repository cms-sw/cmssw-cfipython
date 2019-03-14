import FWCore.ParameterSet.Config as cms

pfDeepDoubleBJetTags = cms.EDProducer('DeepDoubleXTFJetTagsProducer',
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
  flavor = cms.string('B'),
  flav_table = cms.PSet(
    probQ = cms.vuint32(0),
    probH = cms.vuint32(1)
  ),
  src = cms.InputTag('pfDeepDoubleXTagInfosNopt'),
  graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleB/V01/constant_graph_PtCut_MassSculptPen.pb')
)
