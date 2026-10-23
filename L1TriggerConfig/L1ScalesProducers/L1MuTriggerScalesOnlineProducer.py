import FWCore.ParameterSet.Config as cms

def L1MuTriggerScalesOnlineProducer(*args, **kwargs):
  mod = cms.ESProducer('L1MuTriggerScalesOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
