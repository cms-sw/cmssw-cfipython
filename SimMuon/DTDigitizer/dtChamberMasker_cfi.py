import FWCore.ParameterSet.Config as cms

dtChamberMasker = cms.EDProducer('DTChamberMasker',
  digiTag = cms.InputTag('simMuonDTDigis')
)
