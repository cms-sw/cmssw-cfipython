import FWCore.ParameterSet.Config as cms

def NavigateEventsLooper(**kwargs):
  mod = cms.Looper('NavigateEventsLooper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
