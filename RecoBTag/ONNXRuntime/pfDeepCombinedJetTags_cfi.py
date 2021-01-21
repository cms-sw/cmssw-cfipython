import FWCore.ParameterSet.Config as cms

pfDeepCombinedJetTags = cms.EDProducer('DeepCombinedONNXJetTagsProducer',
  src = cms.InputTag('pfDeepFlavourTagInfos'),
  input_names = cms.vstring(
    'input_1_DFla',
    'input_2_DFla',
    'input_3_DFla',
    'input_4_DFla',
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
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepVertex/phase1_deepvertexcombined.onnx'),
  output_names = cms.vstring('dense_13'),
  flav_names = cms.vstring(
    'probb',
    'probc',
    'probuds',
    'probg'
  ),
  min_jet_pt = cms.double(15),
  max_jet_eta = cms.double(2.5)
)
