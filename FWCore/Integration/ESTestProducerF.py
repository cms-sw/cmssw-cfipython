import FWCore.ParameterSet.Config as cms

def ESTestProducerF(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerF',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
