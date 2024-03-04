import FWCore.ParameterSet.Config as cms

def CSCFakeGainsConditions(**kwargs):
  mod = cms.ESSource('CSCFakeGainsConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
