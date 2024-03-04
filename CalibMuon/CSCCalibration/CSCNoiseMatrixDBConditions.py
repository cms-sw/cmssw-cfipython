import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixDBConditions(**kwargs):
  mod = cms.ESSource('CSCNoiseMatrixDBConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
