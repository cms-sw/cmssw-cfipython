import FWCore.ParameterSet.Config as cms

def RPCConfigOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('RPCConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
