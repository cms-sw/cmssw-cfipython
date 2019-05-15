import FWCore.ParameterSet.Config as cms

hltCountNumberOfObjectEdmNewDetSetVectorSiStripMatchedRecHit2D = cms.EDFilter('HLTCountNumberOfMatchedRecHit',
  saveTags = cms.bool(True),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
