import FWCore.ParameterSet.Config as cms

def DummyLooper(**kwargs):
  mod = cms.Looper('DummyLooper',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod