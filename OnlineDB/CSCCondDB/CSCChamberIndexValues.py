import FWCore.ParameterSet.Config as cms

def CSCChamberIndexValues(*args, **kwargs):
  mod = cms.ESSource('CSCChamberIndexValues',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
