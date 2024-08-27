import FWCore.ParameterSet.Config as cms

def KFTrajectoryFitterESProducer(**kwargs):
  mod = cms.ESProducer('KFTrajectoryFitterESProducer',
    ComponentName = cms.string('KFFitter'),
    Propagator = cms.string('PropagatorWithMaterial'),
    Updator = cms.string('KFUpdator'),
    Estimator = cms.string('Chi2'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    minHits = cms.int32(3),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
