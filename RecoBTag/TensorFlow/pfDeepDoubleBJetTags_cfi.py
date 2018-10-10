import FWCore.ParameterSet.Config as cms

pfDeepDoubleBJetTags = cms.EDProducer('DeepDoubleBTFJetTagsProducer',
  src = cms.InputTag('pfDeepDoubleBTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3'
  ),
  graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepDoubleB/V01/constant_graph_PtCut_MassSculptPen.pb'),
  lp_names = cms.vstring('db_input_batchnorm/keras_learning_phase'),
  output_names = cms.vstring('ID_pred/Softmax'),
  flav_table = cms.PSet(
    probQ = cms.vuint32(0),
    probH = cms.vuint32(1)
  ),
  batch_eval = cms.bool(False),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads')
)
