import FWCore.ParameterSet.Config as cms

def GsfTrajectorySmootherESProducer(*args, **kwargs):
  mod = cms.ESProducer('GsfTrajectorySmootherESProducer',
    ComponentName = cms.string('GsfTrajectorySmoother'),
    MaterialEffectsUpdator = cms.string('ElectronMaterialEffects'),
    GeometricalPropagator = cms.string('bwdAnalyticalPropagator'),
    Merger = cms.string('CloseComponentsMerger5D'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    ErrorRescaling = cms.double(100),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
