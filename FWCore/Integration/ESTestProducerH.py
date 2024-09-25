import FWCore.ParameterSet.Config as cms

def ESTestProducerH(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerH',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
