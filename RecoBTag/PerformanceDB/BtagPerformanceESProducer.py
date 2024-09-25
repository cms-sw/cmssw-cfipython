import FWCore.ParameterSet.Config as cms

def BtagPerformanceESProducer(*args, **kwargs):
  mod = cms.ESProducer('BtagPerformanceESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
