import FWCore.ParameterSet.Config as cms

def ProfilerService(*args, **kwargs):
  mod = cms.Service('ProfilerService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
