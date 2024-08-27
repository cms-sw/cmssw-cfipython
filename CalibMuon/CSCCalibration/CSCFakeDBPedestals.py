import FWCore.ParameterSet.Config as cms

def CSCFakeDBPedestals(**kwargs):
  mod = cms.ESSource('CSCFakeDBPedestals',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
