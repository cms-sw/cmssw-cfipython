import FWCore.ParameterSet.Config as cms

def ESTestProducerA(**kwargs):
  mod = cms.ESProducer('ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
