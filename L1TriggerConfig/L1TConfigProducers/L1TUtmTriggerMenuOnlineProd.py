import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('L1TUtmTriggerMenuOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
