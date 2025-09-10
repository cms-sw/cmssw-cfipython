import FWCore.ParameterSet.Config as cms

def ESTestProducerA(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerA',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
