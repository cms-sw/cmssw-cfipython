import FWCore.ParameterSet.Config as cms

def DummyServiceB3(**kwargs):
  mod = cms.Service('DummyServiceB3')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
