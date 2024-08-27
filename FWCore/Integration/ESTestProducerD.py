import FWCore.ParameterSet.Config as cms

def ESTestProducerD(**kwargs):
  mod = cms.ESProducer('ESTestProducerD',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
