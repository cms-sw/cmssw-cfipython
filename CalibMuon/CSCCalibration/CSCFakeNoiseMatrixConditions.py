import FWCore.ParameterSet.Config as cms

def CSCFakeNoiseMatrixConditions(*args, **kwargs):
  mod = cms.ESSource('CSCFakeNoiseMatrixConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
