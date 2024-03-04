import FWCore.ParameterSet.Config as cms

def CSCCrosstalkDBConditions(**kwargs):
  mod = cms.ESSource('CSCCrosstalkDBConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
