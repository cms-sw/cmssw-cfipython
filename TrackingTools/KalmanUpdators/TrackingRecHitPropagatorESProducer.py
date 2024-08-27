import FWCore.ParameterSet.Config as cms

def TrackingRecHitPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('TrackingRecHitPropagatorESProducer',
    ComponentName = cms.required.string,
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
