import FWCore.ParameterSet.Config as cms

def DoodadEDLooper(*args, **kwargs):
  mod = cms.Looper('DoodadEDLooper',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
