import FWCore.ParameterSet.Config as cms

candCountFilter = cms.EDFilter('CandCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0)
)
