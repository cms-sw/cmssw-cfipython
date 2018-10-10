import FWCore.ParameterSet.Config as cms

muonCountFilter = cms.EDFilter('MuonCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
