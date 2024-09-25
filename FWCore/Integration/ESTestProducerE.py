import FWCore.ParameterSet.Config as cms

def ESTestProducerE(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerE',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
