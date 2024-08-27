import FWCore.ParameterSet.Config as cms

def CSCChamberMapValues(**kwargs):
  mod = cms.ESSource('CSCChamberMapValues',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
