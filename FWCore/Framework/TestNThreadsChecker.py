import FWCore.ParameterSet.Config as cms

def TestNThreadsChecker(**kwargs):
  mod = cms.Service('TestNThreadsChecker')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
