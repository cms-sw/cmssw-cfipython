import FWCore.ParameterSet.Config as cms

def L1MuTriggerScaleKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1MuTriggerScaleKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
