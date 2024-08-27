import FWCore.ParameterSet.Config as cms

def CSCGainsConditions(**kwargs):
  mod = cms.ESSource('CSCGainsConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
