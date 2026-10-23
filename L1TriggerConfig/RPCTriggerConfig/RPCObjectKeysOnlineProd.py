import FWCore.ParameterSet.Config as cms

def RPCObjectKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('RPCObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
