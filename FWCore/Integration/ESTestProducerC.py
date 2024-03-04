import FWCore.ParameterSet.Config as cms

def ESTestProducerC(**kwargs):
  mod = cms.ESProducer('ESTestProducerC',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
