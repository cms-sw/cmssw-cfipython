import FWCore.ParameterSet.Config as cms

def DummyLooper(*args, **kwargs):
  mod = cms.Looper('DummyLooper',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
