import FWCore.ParameterSet.Config as cms

def CSCNoiseMatrixDBConditions(*args, **kwargs):
  mod = cms.ESSource('CSCNoiseMatrixDBConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
