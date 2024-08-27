import FWCore.ParameterSet.Config as cms

def RPCConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('RPCConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
