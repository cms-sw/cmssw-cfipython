import FWCore.ParameterSet.Config as cms

pfDeepFlavourJetTags = cms.EDProducer('DeepFlavourTFJetTagsProducer',
  src = cms.InputTag('pfDeepFlavourTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3',
    'input_4',
    'input_5'
  ),
  graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV01_GraphDef_PtCut/constant_graph.pb'),
  lp_names = cms.vstring('globals_input_batchnorm/keras_learning_phase'),
  output_names = cms.vstring(
    'ID_pred/Softmax',
    'regression_pred/BiasAdd'
  ),
  flav_table = cms.PSet(
    probb = cms.vuint32(0),
    probbb = cms.vuint32(1),
    problepb = cms.vuint32(2),
    probc = cms.vuint32(3),
    probuds = cms.vuint32(4),
    probg = cms.vuint32(5)
  ),
  batch_eval = cms.bool(False),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads')
)
