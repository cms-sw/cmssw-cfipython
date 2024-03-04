import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuESProducer(**kwargs):
  mod = cms.ESProducer('L1TUtmTriggerMenuESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
