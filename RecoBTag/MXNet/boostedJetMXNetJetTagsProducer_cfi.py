import FWCore.ParameterSet.Config as cms

boostedJetMXNetJetTagsProducer = cms.EDProducer('BoostedJetMXNetJetTagsProducer',
  src = cms.InputTag('pfDeepBoostedJetTagInfos'),
  preprocessParams = cms.PSet(),
  model_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V01/full/resnet-symbol.json'),
  param_path = cms.FileInPath('RecoBTag/Combined/data/DeepBoostedJet/V01/full/resnet-0000.params'),
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
  debugMode = cms.untracked.bool(False)
)
