import FWCore.ParameterSet.Config as cms

def ESTestProducerF(**kwargs):
  mod = cms.ESProducer('ESTestProducerF',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
