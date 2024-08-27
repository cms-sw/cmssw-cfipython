import FWCore.ParameterSet.Config as cms

def DummyServiceD2(**kwargs):
  mod = cms.Service('DummyServiceD2')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
