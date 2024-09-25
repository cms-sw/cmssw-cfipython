import FWCore.ParameterSet.Config as cms

def CSCFakeDBPedestals(*args, **kwargs):
  mod = cms.ESSource('CSCFakeDBPedestals',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
