import FWCore.ParameterSet.Config as cms

def RPCFakeCalibration(*args, **kwargs):
  mod = cms.ESSource('RPCFakeCalibration',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
