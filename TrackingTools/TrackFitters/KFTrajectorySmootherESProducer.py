import FWCore.ParameterSet.Config as cms

def KFTrajectorySmootherESProducer(*args, **kwargs):
  mod = cms.ESProducer('KFTrajectorySmootherESProducer',
    ComponentName = cms.string('KFSmoother'),
    Propagator = cms.string('PropagatorWithMaterial'),
    Updator = cms.string('KFUpdator'),
    Estimator = cms.string('Chi2'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    errorRescaling = cms.double(100),
    minHits = cms.int32(3),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
