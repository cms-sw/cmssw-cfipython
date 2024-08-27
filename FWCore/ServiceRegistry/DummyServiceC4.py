import FWCore.ParameterSet.Config as cms

def DummyServiceC4(**kwargs):
  mod = cms.Service('DummyServiceC4')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
