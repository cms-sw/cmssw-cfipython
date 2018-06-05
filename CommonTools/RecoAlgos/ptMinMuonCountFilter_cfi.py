import FWCore.ParameterSet.Config as cms

ptMinMuonCountFilter = cms.EDFilter('PtMinMuonCountFilter',
  src = cms.InputTag(''),
  ptMin = cms.double(0),
  minNumber = cms.uint32(0)
)
