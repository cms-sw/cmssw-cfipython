import FWCore.ParameterSet.Config as cms

def IterateNTimesLooper(**kwargs):
  mod = cms.Looper('IterateNTimesLooper')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
