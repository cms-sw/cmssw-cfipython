import FWCore.ParameterSet.Config as cms

def DummyServiceE0(*args, **kwargs):
  mod = cms.Service('DummyServiceE0')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
