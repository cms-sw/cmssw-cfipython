import FWCore.ParameterSet.Config as cms

def CSCFakeDBCrosstalk(*args, **kwargs):
  mod = cms.ESSource('CSCFakeDBCrosstalk',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
