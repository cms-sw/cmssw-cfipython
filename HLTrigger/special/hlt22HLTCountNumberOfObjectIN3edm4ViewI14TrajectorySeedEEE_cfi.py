import FWCore.ParameterSet.Config as cms

hlt22HLTCountNumberOfObjectIN3edm4ViewI14TrajectorySeedEEE = cms.EDFilter('HLTCountNumberOfTrajectorySeed',
  saveTags = cms.bool(False),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
