import FWCore.ParameterSet.Config as cms

GEMDigiSource = cms.EDProducer('GEMDigiSource',
  digisInputLabel = cms.InputTag('muonGEMDigis'),
  logCategory = cms.untracked.string('GEMDigiSource'),
  modeRelVal = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
