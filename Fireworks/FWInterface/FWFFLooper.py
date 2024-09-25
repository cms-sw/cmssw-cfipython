import FWCore.ParameterSet.Config as cms

def FWFFLooper(*args, **kwargs):
  mod = cms.Looper('FWFFLooper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
