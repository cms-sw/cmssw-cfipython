import FWCore.ParameterSet.Config as cms

def DummyStoreConfigService(*args, **kwargs):
  mod = cms.Service('DummyStoreConfigService')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
