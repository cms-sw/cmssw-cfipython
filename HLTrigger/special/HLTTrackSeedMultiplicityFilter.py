import FWCore.ParameterSet.Config as cms

def HLTTrackSeedMultiplicityFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTTrackSeedMultiplicityFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('hltRegionalCosmicTrackerSeeds'),
    minSeeds = cms.uint32(0),
    maxSeeds = cms.uint32(10000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
