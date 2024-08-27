import FWCore.ParameterSet.Config as cms

def CSCGainsDBConditions(**kwargs):
  mod = cms.ESSource('CSCGainsDBConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
