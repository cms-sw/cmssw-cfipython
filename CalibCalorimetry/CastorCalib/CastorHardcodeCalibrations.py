import FWCore.ParameterSet.Config as cms

def CastorHardcodeCalibrations(**kwargs):
  mod = cms.ESSource('CastorHardcodeCalibrations',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
