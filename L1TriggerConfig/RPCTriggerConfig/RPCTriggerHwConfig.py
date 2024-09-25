import FWCore.ParameterSet.Config as cms

def RPCTriggerHwConfig(*args, **kwargs):
  mod = cms.ESProducer('RPCTriggerHwConfig',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
