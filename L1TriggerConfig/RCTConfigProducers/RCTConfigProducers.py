import FWCore.ParameterSet.Config as cms

def RCTConfigProducers(*args, **kwargs):
  mod = cms.ESProducer('RCTConfigProducers',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
