import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuObjectKeysOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TUtmTriggerMenuObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
