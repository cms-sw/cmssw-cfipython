import FWCore.ParameterSet.Config as cms

def TrackSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
