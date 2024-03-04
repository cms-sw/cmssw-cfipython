import FWCore.ParameterSet.Config as cms

def MTDTransientTrackingRecHitBuilderESProducer(**kwargs):
  mod = cms.ESProducer('MTDTransientTrackingRecHitBuilderESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
