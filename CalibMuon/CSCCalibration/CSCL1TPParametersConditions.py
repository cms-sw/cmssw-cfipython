import FWCore.ParameterSet.Config as cms

def CSCL1TPParametersConditions(**kwargs):
  mod = cms.ESSource('CSCL1TPParametersConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
