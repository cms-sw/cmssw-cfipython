import FWCore.ParameterSet.Config as cms

def DummyServiceA1(**kwargs):
  mod = cms.Service('DummyServiceA1')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
