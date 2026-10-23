import FWCore.ParameterSet.Config as cms

def L1MuTriggerPtScaleOnlineProducer(*args, **kwargs):
  mod = cms.ESProducer('L1MuTriggerPtScaleOnlineProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
