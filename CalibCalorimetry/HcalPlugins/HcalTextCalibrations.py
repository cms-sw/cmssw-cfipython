import FWCore.ParameterSet.Config as cms

def HcalTextCalibrations(*args, **kwargs):
  mod = cms.ESSource('HcalTextCalibrations',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
