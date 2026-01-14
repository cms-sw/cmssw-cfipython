import FWCore.ParameterSet.Config as cms

def NavigateEventsLooper(*args, **kwargs):
  mod = cms.Looper('NavigateEventsLooper',
    maxLoops = cms.untracked.int32(-1)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
