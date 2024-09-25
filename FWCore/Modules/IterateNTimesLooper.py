import FWCore.ParameterSet.Config as cms

def IterateNTimesLooper(*args, **kwargs):
  mod = cms.Looper('IterateNTimesLooper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
