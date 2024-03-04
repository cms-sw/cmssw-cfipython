import FWCore.ParameterSet.Config as cms

def RPCTriggerConfig(**kwargs):
  mod = cms.ESProducer('RPCTriggerConfig',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
