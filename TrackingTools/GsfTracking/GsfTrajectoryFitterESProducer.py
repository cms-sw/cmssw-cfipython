import FWCore.ParameterSet.Config as cms

def GsfTrajectoryFitterESProducer(*args, **kwargs):
  mod = cms.ESProducer('GsfTrajectoryFitterESProducer',
    ComponentName = cms.required.string,
    MaterialEffectsUpdator = cms.required.string,
    GeometricalPropagator = cms.required.string,
    Merger = cms.required.string,
    RecoGeometry = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
