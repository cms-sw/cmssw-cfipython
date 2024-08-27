import FWCore.ParameterSet.Config as cms

def L1TriggerKeyDummyProdExt(**kwargs):
  mod = cms.ESProducer('L1TriggerKeyDummyProdExt',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
