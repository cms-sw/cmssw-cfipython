import FWCore.ParameterSet.Config as cms

def KFTrajectoryFitterESProducer(*args, **kwargs):
  mod = cms.ESProducer('KFTrajectoryFitterESProducer',
    ComponentName = cms.string('KFFitter'),
    Propagator = cms.string('PropagatorWithMaterial'),
    Updator = cms.string('KFUpdator'),
    Estimator = cms.string('Chi2'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    minHits = cms.int32(3),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
