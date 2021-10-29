import FWCore.ParameterSet.Config as cms

numberPerLSFilter = cms.EDFilter('NumberPerLSFilter',
  maxN = cms.int32(100),
  mightGet = cms.optional.untracked.vstring
)
