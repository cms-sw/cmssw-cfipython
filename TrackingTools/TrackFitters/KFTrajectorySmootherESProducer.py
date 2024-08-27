import FWCore.ParameterSet.Config as cms

def KFTrajectorySmootherESProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
