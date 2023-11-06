import FWCore.ParameterSet.Config as cms

GEMDigiSource = cms.EDProducer('GEMDigiSource',
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  runType = cms.untracked.string('online'),
  logCategory = cms.untracked.string('GEMDigiSource'),
  bxMin = cms.int32(-10),
  bxMax = cms.int32(10),
  useDBEMap = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
