import FWCore.ParameterSet.Config as cms

def TrackingFailureFilter(*args, **kwargs):
  mod = cms.EDFilter('TrackingFailureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
