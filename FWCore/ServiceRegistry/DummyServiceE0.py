import FWCore.ParameterSet.Config as cms

def DummyServiceE0(**kwargs):
  mod = cms.Service('DummyServiceE0')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
