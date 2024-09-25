import FWCore.ParameterSet.Config as cms

def ESTestProducerG(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerG',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
