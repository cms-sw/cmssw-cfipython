import FWCore.ParameterSet.Config as cms

def ESTestProducerBUsingHost(**kwargs):
  mod = cms.ESProducer('ESTestProducerBUsingHost',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
