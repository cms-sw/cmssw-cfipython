import FWCore.ParameterSet.Config as cms

def ESTestProducerB(**kwargs):
  mod = cms.ESProducer('ESTestProducerB',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
