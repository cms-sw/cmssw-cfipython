import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixConditions(**kwargs):
  mod = cms.ESSource('CSCNoiseMatrixConditions',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
