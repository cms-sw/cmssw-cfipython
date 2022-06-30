import FWCore.ParameterSet.Config as cms

particleNetSonicJetTagsProducer = cms.EDProducer('ParticleNetSonicJetTagsProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    verbose = cms.untracked.bool(False),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    useSharedMemory = cms.untracked.bool(True),
    compression = cms.untracked.string(''),
    outputs = cms.untracked.vstring()
  ),
  src = cms.InputTag('pfDeepBoostedJetTagInfos'),
  preprocess_json = cms.string(''),
  preprocessParams = cms.PSet(),
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
  debugMode = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
