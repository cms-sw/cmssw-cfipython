import FWCore.ParameterSet.Config as cms

def DummyServiceB3(*args, **kwargs):
  mod = cms.Service('DummyServiceB3')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
