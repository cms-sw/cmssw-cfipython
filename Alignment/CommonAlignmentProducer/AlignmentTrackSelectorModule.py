import FWCore.ParameterSet.Config as cms

def AlignmentTrackSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
