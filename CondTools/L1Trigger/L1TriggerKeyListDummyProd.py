import FWCore.ParameterSet.Config as cms

def L1TriggerKeyListDummyProd(*args, **kwargs):
  mod = cms.ESProducer('L1TriggerKeyListDummyProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
