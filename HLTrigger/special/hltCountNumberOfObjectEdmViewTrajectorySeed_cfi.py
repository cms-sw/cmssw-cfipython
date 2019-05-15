import FWCore.ParameterSet.Config as cms

hltCountNumberOfObjectEdmViewTrajectorySeed = cms.EDFilter('HLTCountNumberOfTrajectorySeed',
  saveTags = cms.bool(True),
  src = cms.InputTag(''),
  MinN = cms.int32(0),
  MaxN = cms.int32(99999)
)
