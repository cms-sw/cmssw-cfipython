import FWCore.ParameterSet.Config as cms

def CSCCrateMapValues(**kwargs):
  mod = cms.ESSource('CSCCrateMapValues',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
