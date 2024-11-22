import FWCore.ParameterSet.Config as cms

def ESTestProducerI(*args, **kwargs):
  mod = cms.ESProducer('ESTestProducerI',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
