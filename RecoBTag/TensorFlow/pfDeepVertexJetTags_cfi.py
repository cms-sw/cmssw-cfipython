import FWCore.ParameterSet.Config as cms

pfDeepVertexJetTags = cms.EDProducer('DeepVertexTFJetTagsProducer',
  src = cms.InputTag('pfDeepFlavourTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3',
    'input_4',
    'input_5',
    'input_6',
    'input_7',
    'input_8',
    'input_9',
    'input_10',
    'input_11',
    'input_12'
  ),
  graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepVertex/Converted_retraining.pb'),
  lp_names = cms.vstring(),
  output_names = cms.vstring('output_node0'),
  flav_table = cms.PSet(
    probb = cms.vuint32(0),
    probc = cms.vuint32(1),
    probuds = cms.vuint32(2),
    probg = cms.vuint32(3)
  ),
  batch_eval = cms.bool(False),
  min_jet_pt = cms.double(15),
  max_jet_eta = cms.double(2.5),
  nThreads = cms.uint32(1),
  singleThreadPool = cms.string('no_threads'),
  mightGet = cms.optional.untracked.vstring
)
