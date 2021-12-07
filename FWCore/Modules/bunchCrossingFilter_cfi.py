import FWCore.ParameterSet.Config as cms

bunchCrossingFilter = cms.EDFilter('BunchCrossingFilter',
  bunches = cms.vuint32(),
  mightGet = cms.optional.untracked.vstring
)
