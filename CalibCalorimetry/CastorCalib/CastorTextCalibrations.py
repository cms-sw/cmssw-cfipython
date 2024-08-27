import FWCore.ParameterSet.Config as cms

def CastorTextCalibrations(**kwargs):
  mod = cms.ESSource('CastorTextCalibrations',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
