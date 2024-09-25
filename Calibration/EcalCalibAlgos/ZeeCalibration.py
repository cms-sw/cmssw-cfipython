import FWCore.ParameterSet.Config as cms

def ZeeCalibration(*args, **kwargs):
  mod = cms.Looper('ZeeCalibration',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
