import FWCore.ParameterSet.Config as cms

hlt22HLTCountNumberOfObjectIN6edmNew12DetSetVectorI15SiStripRecHit2DEEE = cms.EDFilter('HLTCountNumberOfSingleRecHit',
  saveTags = cms.bool(False),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
