import FWCore.ParameterSet.Config as cms

def CSCGainsConditions(*args, **kwargs):
  mod = cms.ESSource('CSCGainsConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
