import FWCore.ParameterSet.Config as cms

hlt22HLTCountNumberOfObjectIN6edmNew12DetSetVectorI22SiStripMatchedRecHit2DEEE = cms.EDFilter('HLTCountNumberOfMatchedRecHit',
  saveTags = cms.bool(False),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
