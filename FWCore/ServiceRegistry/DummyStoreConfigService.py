import FWCore.ParameterSet.Config as cms

def DummyStoreConfigService(**kwargs):
  mod = cms.Service('DummyStoreConfigService')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
