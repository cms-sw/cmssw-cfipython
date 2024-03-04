import FWCore.ParameterSet.Config as cms

def ESTestProducerE(**kwargs):
  mod = cms.ESProducer('ESTestProducerE',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
