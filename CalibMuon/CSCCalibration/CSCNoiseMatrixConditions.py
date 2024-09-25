import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixConditions(*args, **kwargs):
  mod = cms.ESSource('CSCNoiseMatrixConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
