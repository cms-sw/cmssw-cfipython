import FWCore.ParameterSet.Config as cms

hltCountNumberOfObjectEdmNewDetSetVectorSiStripRecHit2D = cms.EDFilter('HLTCountNumberOfSingleRecHit',
  saveTags = cms.bool(True),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
