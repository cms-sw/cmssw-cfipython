import FWCore.ParameterSet.Config as cms

dtChamberMasker = cms.EDProducer('DTChamberMasker',
  digiTag = cms.InputTag('simMuonDTDigis'),
  mightGet = cms.optional.untracked.vstring
)
