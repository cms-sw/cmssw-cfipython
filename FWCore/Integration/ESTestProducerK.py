import FWCore.ParameterSet.Config as cms

def ESTestProducerK(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerK',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
