import FWCore.ParameterSet.Config as cms

def RPCTriggerBxOrConfig(**kwargs):
  mod = cms.ESProducer('RPCTriggerBxOrConfig',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
