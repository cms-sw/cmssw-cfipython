import FWCore.ParameterSet.Config as cms

def RPCTriggerConfig(*args, **kwargs):
  mod = cms.ESProducer('RPCTriggerConfig',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
