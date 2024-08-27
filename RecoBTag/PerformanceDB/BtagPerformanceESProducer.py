import FWCore.ParameterSet.Config as cms

def BtagPerformanceESProducer(**kwargs):
  mod = cms.ESProducer('BtagPerformanceESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
