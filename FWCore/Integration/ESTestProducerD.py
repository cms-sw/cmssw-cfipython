import FWCore.ParameterSet.Config as cms

def ESTestProducerD(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerD',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
