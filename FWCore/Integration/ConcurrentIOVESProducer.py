import FWCore.ParameterSet.Config as cms

def ConcurrentIOVESProducer(**kwargs):
  mod = cms.ESProducer('ConcurrentIOVESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
