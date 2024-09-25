import FWCore.ParameterSet.Config as cms

def CalibrationTrackSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('CalibrationTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
