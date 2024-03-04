import FWCore.ParameterSet.Config as cms

def RPCObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('RPCObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
