import FWCore.ParameterSet.Config as cms

bunchCrossingFilter = cms.EDFilter('BunchCrossingFilter',
  bunches = cms.vuint32()
)
