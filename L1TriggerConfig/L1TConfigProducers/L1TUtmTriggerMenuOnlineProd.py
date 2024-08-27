import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TUtmTriggerMenuOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
