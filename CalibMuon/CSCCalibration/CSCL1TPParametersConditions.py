import FWCore.ParameterSet.Config as cms

def CSCL1TPParametersConditions(*args, **kwargs):
  mod = cms.ESSource('CSCL1TPParametersConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
