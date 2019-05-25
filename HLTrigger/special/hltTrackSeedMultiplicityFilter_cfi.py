import FWCore.ParameterSet.Config as cms

hltTrackSeedMultiplicityFilter = cms.EDFilter('HLTTrackSeedMultiplicityFilter',
  saveTags = cms.bool(True),
  inputTag = cms.InputTag('hltRegionalCosmicTrackerSeeds'),
  minSeeds = cms.uint32(0),
  maxSeeds = cms.uint32(10000)
)
