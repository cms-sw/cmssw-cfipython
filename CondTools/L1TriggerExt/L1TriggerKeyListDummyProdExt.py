import FWCore.ParameterSet.Config as cms

def L1TriggerKeyListDummyProdExt(**kwargs):
  mod = cms.ESProducer('L1TriggerKeyListDummyProdExt',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
