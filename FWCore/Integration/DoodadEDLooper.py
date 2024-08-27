import FWCore.ParameterSet.Config as cms

def DoodadEDLooper(**kwargs):
  mod = cms.Looper('DoodadEDLooper',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
