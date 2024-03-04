import FWCore.ParameterSet.Config as cms

def HLTTrackSeedMultiplicityFilter(**kwargs):
  mod = cms.EDFilter('HLTTrackSeedMultiplicityFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltRegionalCosmicTrackerSeeds'),
    minSeeds = cms.uint32(0),
    maxSeeds = cms.uint32(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
