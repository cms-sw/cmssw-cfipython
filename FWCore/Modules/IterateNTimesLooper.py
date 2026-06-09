import FWCore.ParameterSet.Config as cms

def IterateNTimesLooper(*args, **kwargs):
  mod = cms.Looper('IterateNTimesLooper',
    nTimes = cms.required.uint32
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
