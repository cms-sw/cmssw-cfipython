import FWCore.ParameterSet.Config as cms

booleanFilter = cms.EDFilter('BooleanFilter',
  src = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring
)
