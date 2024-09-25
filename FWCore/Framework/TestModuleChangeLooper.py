import FWCore.ParameterSet.Config as cms

def TestModuleChangeLooper(*args, **kwargs):
  mod = cms.Looper('TestModuleChangeLooper')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
