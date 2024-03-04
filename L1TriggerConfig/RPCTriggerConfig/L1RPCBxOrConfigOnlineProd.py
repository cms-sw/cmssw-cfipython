import FWCore.ParameterSet.Config as cms

def L1RPCBxOrConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1RPCBxOrConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
