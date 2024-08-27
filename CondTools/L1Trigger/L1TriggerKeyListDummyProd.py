import FWCore.ParameterSet.Config as cms

def L1TriggerKeyListDummyProd(**kwargs):
  mod = cms.ESProducer('L1TriggerKeyListDummyProd',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
