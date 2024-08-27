import FWCore.ParameterSet.Config as cms

def DummyService(**kwargs):
  mod = cms.Service('DummyService',
    value = cms.required.int32
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
