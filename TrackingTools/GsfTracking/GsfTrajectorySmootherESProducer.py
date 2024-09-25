import FWCore.ParameterSet.Config as cms

def GsfTrajectorySmootherESProducer(*args, **kwargs):
  mod = cms.ESProducer('GsfTrajectorySmootherESProducer',
    ComponentName = cms.required.string,
    MaterialEffectsUpdator = cms.required.string,
    GeometricalPropagator = cms.required.string,
    Merger = cms.required.string,
    RecoGeometry = cms.required.string,
    ErrorRescaling = cms.required.double,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
