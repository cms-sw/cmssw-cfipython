import FWCore.ParameterSet.Config as cms

def AlignmentSeedSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentSeedSelectorModule',
    src = cms.InputTag(''),
    applySeedNumber = cms.bool(False),
    minNSeeds = cms.int32(0),
    maxNSeeds = cms.int32(999999),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
