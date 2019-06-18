import FWCore.ParameterSet.Config as cms

candCountFilter = cms.EDFilter('CandCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
