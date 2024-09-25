import FWCore.ParameterSet.Config as cms

def NavigateEventsLooper(*args, **kwargs):
  mod = cms.Looper('NavigateEventsLooper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
