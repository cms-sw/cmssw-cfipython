import FWCore.ParameterSet.Config as cms

def SiTrackerMultiRecHitUpdatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('SiTrackerMultiRecHitUpdatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
