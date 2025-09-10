import FWCore.ParameterSet.Config as cms

def CSCCrateMapValues(*args, **kwargs):
  mod = cms.ESSource('CSCCrateMapValues',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
