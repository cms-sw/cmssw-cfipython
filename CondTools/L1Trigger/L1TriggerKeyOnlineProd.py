import FWCore.ParameterSet.Config as cms

def L1TriggerKeyOnlineProd(**kwargs):
  mod = cms.ESProducer('L1TriggerKeyOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
