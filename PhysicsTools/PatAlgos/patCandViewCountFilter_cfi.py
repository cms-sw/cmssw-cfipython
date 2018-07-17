import FWCore.ParameterSet.Config as cms

patCandViewCountFilter = cms.EDFilter('PATCandViewCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  maxNumber = cms.uint32(0)
)
