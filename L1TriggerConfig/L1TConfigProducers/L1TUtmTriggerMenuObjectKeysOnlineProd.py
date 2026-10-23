import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuObjectKeysOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1TUtmTriggerMenuObjectKeysOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
