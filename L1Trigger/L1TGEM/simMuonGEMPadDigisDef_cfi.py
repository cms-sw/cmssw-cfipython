import FWCore.ParameterSet.Config as cms

simMuonGEMPadDigisDef = cms.EDProducer('GEMPadDigiProducer',
  InputCollection = cms.InputTag('simMuonGEMDigis'),
  use16GE21 = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
