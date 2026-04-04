import FWCore.ParameterSet.Config as cms

def DummyServiceD2(*args, **kwargs):
  mod = cms.Service('DummyServiceD2')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
