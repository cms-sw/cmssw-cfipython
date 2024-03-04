import FWCore.ParameterSet.Config as cms

def CSCCrosstalkConditions(**kwargs):
  mod = cms.ESSource('CSCCrosstalkConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
