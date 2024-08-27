import FWCore.ParameterSet.Config as cms

def CSCFakeDBCrosstalk(**kwargs):
  mod = cms.ESSource('CSCFakeDBCrosstalk',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
