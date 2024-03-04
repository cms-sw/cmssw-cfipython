import FWCore.ParameterSet.Config as cms

def GsfTrajectoryFitterESProducer(**kwargs):
  mod = cms.ESProducer('GsfTrajectoryFitterESProducer',
    ComponentName = cms.required.string,
    MaterialEffectsUpdator = cms.required.string,
    GeometricalPropagator = cms.required.string,
    Merger = cms.required.string,
    RecoGeometry = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
