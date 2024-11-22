import FWCore.ParameterSet.Config as cms

def ESTestProducerB(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerB',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
