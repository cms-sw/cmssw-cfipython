import FWCore.ParameterSet.Config as cms

def HcalTextCalibrations(**kwargs):
  mod = cms.ESSource('HcalTextCalibrations',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
