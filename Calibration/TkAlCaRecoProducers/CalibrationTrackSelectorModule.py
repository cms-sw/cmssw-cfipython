import FWCore.ParameterSet.Config as cms

def CalibrationTrackSelectorModule(**kwargs):
  mod = cms.EDFilter('CalibrationTrackSelectorModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
