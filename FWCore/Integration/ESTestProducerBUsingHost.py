import FWCore.ParameterSet.Config as cms

def ESTestProducerBUsingHost(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerBUsingHost',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
