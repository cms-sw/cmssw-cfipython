import FWCore.ParameterSet.Config as cms

def L1TriggerKeyDummyProd(**kwargs):
  mod = cms.ESProducer('L1TriggerKeyDummyProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
