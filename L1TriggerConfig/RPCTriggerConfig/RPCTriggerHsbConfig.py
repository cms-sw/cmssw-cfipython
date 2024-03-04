import FWCore.ParameterSet.Config as cms

def RPCTriggerHsbConfig(**kwargs):
  mod = cms.ESProducer('RPCTriggerHsbConfig',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
