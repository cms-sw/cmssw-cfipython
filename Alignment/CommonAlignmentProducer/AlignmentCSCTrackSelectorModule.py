import FWCore.ParameterSet.Config as cms

def AlignmentCSCTrackSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentCSCTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
