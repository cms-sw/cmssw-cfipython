import FWCore.ParameterSet.Config as cms

def ConcurrentIOVESProducer(*args, **kwargs):
  mod = cms.ESProducer('ConcurrentIOVESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
