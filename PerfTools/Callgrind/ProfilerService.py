import FWCore.ParameterSet.Config as cms

def ProfilerService(**kwargs):
  mod = cms.Service('ProfilerService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
