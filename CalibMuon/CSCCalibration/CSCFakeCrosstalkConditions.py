import FWCore.ParameterSet.Config as cms

def CSCFakeCrosstalkConditions(*args, **kwargs):
  mod = cms.ESSource('CSCFakeCrosstalkConditions',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
