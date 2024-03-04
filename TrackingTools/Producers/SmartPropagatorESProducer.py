import FWCore.ParameterSet.Config as cms

def SmartPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('SmartPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
