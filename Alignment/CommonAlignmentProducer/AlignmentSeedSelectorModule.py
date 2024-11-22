import FWCore.ParameterSet.Config as cms

def AlignmentSeedSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentSeedSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
