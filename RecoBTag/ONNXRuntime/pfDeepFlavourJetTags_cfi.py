import FWCore.ParameterSet.Config as cms

pfDeepFlavourJetTags = cms.EDProducer('DeepFlavourONNXJetTagsProducer',
  src = cms.InputTag('pfDeepFlavourTagInfos'),
  input_names = cms.vstring(
    'input_1',
    'input_2',
    'input_3',
    'input_4',
    'input_5'
  ),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/model.onnx'),
  output_names = cms.vstring('ID_pred/Softmax:0'),
  flav_names = cms.vstring(
    'probb',
    'probbb',
    'problepb',
    'probc',
    'probuds',
    'probg'
  )
)
