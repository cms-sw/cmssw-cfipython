import FWCore.ParameterSet.Config as cms

def RPCTriggerBxOrConfig(*args, **kwargs):
  mod = cms.ESProducer('RPCTriggerBxOrConfig',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
