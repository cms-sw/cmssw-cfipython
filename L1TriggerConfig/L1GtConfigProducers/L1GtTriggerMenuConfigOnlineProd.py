import FWCore.ParameterSet.Config as cms

def L1GtTriggerMenuConfigOnlineProd(**kwargs):
  mod = cms.ESProducer('L1GtTriggerMenuConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
