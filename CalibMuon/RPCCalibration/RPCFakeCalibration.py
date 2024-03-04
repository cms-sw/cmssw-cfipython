import FWCore.ParameterSet.Config as cms

def RPCFakeCalibration(**kwargs):
  mod = cms.ESSource('RPCFakeCalibration',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
