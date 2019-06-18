import FWCore.ParameterSet.Config as cms

candViewCountFilter = cms.EDFilter('CandViewCountFilter',
  src = cms.InputTag(''),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
