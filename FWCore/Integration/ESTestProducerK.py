import FWCore.ParameterSet.Config as cms

def ESTestProducerK(**kwargs):
  mod = cms.ESProducer('ESTestProducerK',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
