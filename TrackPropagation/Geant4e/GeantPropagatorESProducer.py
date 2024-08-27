import FWCore.ParameterSet.Config as cms

def GeantPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('GeantPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
