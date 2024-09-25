import FWCore.ParameterSet.Config as cms

def ESTestProducerJ(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerJ',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
