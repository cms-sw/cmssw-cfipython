import FWCore.ParameterSet.Config as cms

def CSCChamberMapValues(*args, **kwargs):
  mod = cms.ESSource('CSCChamberMapValues',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
