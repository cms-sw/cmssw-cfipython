import FWCore.ParameterSet.Config as cms

def MultiRecHitCollectorESProducer(*args, **kwargs):
  mod = cms.ESProducer('MultiRecHitCollectorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
