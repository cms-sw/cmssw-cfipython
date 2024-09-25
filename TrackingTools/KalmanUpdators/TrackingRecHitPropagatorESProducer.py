import FWCore.ParameterSet.Config as cms

def TrackingRecHitPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('TrackingRecHitPropagatorESProducer',
    ComponentName = cms.required.string,
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
