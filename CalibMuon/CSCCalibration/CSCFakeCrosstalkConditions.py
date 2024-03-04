import FWCore.ParameterSet.Config as cms

def CSCFakeCrosstalkConditions(**kwargs):
  mod = cms.ESSource('CSCFakeCrosstalkConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
