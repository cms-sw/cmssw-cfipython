import FWCore.ParameterSet.Config as cms

def CSCGainsDBConditions(*args, **kwargs):
  mod = cms.ESSource('CSCGainsDBConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
