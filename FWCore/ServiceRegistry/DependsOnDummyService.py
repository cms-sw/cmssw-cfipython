import FWCore.ParameterSet.Config as cms

def DependsOnDummyService(*args, **kwargs):
  mod = cms.Service('DependsOnDummyService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
