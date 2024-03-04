import FWCore.ParameterSet.Config as cms

def ESTestProducerH(**kwargs):
  mod = cms.ESProducer('ESTestProducerH',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
