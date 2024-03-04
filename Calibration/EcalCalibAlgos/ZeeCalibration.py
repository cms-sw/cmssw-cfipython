import FWCore.ParameterSet.Config as cms

def ZeeCalibration(**kwargs):
  mod = cms.EDLooper('ZeeCalibration',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
