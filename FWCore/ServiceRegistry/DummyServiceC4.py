import FWCore.ParameterSet.Config as cms

def DummyServiceC4(*args, **kwargs):
  mod = cms.Service('DummyServiceC4')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
