import FWCore.ParameterSet.Config as cms

def ESTestProducerAZ(**kwargs):
  mod = cms.ESProducer('ESTestProducerAZ',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
