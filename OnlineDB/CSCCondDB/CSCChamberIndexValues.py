import FWCore.ParameterSet.Config as cms

def CSCChamberIndexValues(**kwargs):
  mod = cms.ESSource('CSCChamberIndexValues',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
