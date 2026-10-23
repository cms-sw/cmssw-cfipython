import FWCore.ParameterSet.Config as cms

def DummyService(*args, **kwargs):
  mod = cms.Service('DummyService',
    value = cms.required.int32
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
