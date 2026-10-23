import FWCore.ParameterSet.Config as cms

def TestNThreadsChecker(*args, **kwargs):
  mod = cms.Service('TestNThreadsChecker')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
