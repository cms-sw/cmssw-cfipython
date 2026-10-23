import FWCore.ParameterSet.Config as cms

def CSCCrosstalkDBConditions(*args, **kwargs):
  mod = cms.ESSource('CSCCrosstalkDBConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
