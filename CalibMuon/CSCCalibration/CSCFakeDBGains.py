import FWCore.ParameterSet.Config as cms

def CSCFakeDBGains(*args, **kwargs):
  mod = cms.ESSource('CSCFakeDBGains',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
