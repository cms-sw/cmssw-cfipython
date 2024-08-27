import FWCore.ParameterSet.Config as cms

def DependsOnDummyService(**kwargs):
  mod = cms.Service('DependsOnDummyService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
