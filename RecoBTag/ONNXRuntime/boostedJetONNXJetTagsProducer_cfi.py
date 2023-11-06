import FWCore.ParameterSet.Config as cms

boostedJetONNXJetTagsProducer = cms.EDProducer('BoostedJetONNXJetTagsProducer',
  src = cms.InputTag('pfDeepBoostedJetTagInfos'),
  preprocess_json = cms.string(''),
  preprocessParams = cms.PSet(),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V02/full/resnet.onnx'),
  flav_names = cms.vstring(
    'probTbcq',
    'probTbqq',
    'probTbc',
    'probTbq',
    'probWcq',
    'probWqq',
    'probZbb',
    'probZcc',
    'probZqq',
    'probHbb',
    'probHcc',
    'probHqqqq',
    'probQCDbb',
    'probQCDcc',
    'probQCDb',
    'probQCDc',
    'probQCDothers'
  ),
  jets = cms.InputTag(''),
  produceValueMap = cms.untracked.bool(False),
  debugMode = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
