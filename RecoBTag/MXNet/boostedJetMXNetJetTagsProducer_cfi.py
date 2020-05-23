import FWCore.ParameterSet.Config as cms

boostedJetMXNetJetTagsProducer = cms.EDProducer('BoostedJetMXNetJetTagsProducer',
  src = cms.InputTag('pfParticleNetTagInfos'),
  preprocessParams = cms.PSet(),
  model_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/General/V00/ParticleNet-symbol.json'),
  param_path = cms.FileInPath('RecoBTag/Combined/data/ParticleNetAK8/General/V00/ParticleNet-0000.params'),
  flav_names = cms.vstring(
    'probTbcq',
    'probTbqq',
    'probTbc',
    'probTbq',
    'probTbel',
    'probTbmu',
    'probTbta',
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
  debugMode = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
