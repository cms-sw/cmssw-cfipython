import FWCore.ParameterSet.Config as cms

caloJetCountFilter = cms.EDFilter('CaloJetCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
