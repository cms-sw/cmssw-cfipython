import FWCore.ParameterSet.Config as cms

def ESTestProducerI(**kwargs):
  mod = cms.ESProducer('ESTestProducerI',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
