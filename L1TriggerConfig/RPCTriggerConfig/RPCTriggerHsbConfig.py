import FWCore.ParameterSet.Config as cms

def RPCTriggerHsbConfig(*args, **kwargs):
  mod = cms.ESProducer('RPCTriggerHsbConfig',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
