import FWCore.ParameterSet.Config as cms

def CastorHardcodeCalibrations(*args, **kwargs):
  mod = cms.ESSource('CastorHardcodeCalibrations',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
