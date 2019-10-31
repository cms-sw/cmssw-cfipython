import FWCore.ParameterSet.Config as cms

simMuonGEMPadDigisDef = cms.EDProducer('GEMPadDigiProducer',
  InputCollection = cms.InputTag('simMuonGEMDigis'),
  mightGet = cms.optional.untracked.vstring
)
