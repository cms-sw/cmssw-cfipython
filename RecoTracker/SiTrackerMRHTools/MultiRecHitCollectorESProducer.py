import FWCore.ParameterSet.Config as cms

def MultiRecHitCollectorESProducer(**kwargs):
  mod = cms.ESProducer('MultiRecHitCollectorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
