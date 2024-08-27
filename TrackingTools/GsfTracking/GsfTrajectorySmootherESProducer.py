import FWCore.ParameterSet.Config as cms

def GsfTrajectorySmootherESProducer(**kwargs):
  mod = cms.ESProducer('GsfTrajectorySmootherESProducer',
    ComponentName = cms.required.string,
    MaterialEffectsUpdator = cms.required.string,
    GeometricalPropagator = cms.required.string,
    Merger = cms.required.string,
    RecoGeometry = cms.required.string,
    ErrorRescaling = cms.required.double,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
