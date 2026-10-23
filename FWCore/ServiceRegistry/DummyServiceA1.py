import FWCore.ParameterSet.Config as cms

def DummyServiceA1(*args, **kwargs):
  mod = cms.Service('DummyServiceA1')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
