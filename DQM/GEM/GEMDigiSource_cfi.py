import FWCore.ParameterSet.Config as cms

GEMDigiSource = cms.EDProducer('GEMDigiSource',
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  logCategory = cms.untracked.string('GEMDigiSource'),
  modeRelVal = cms.bool(False),
  bxMin = cms.int32(-10),
  bxMax = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)
