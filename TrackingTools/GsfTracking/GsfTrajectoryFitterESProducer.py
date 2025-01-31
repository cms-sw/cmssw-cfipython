import FWCore.ParameterSet.Config as cms

def GsfTrajectoryFitterESProducer(*args, **kwargs):
  mod = cms.ESProducer('GsfTrajectoryFitterESProducer',
    ComponentName = cms.string('GsfTrajectoryFitter'),
    MaterialEffectsUpdator = cms.string('ElectronMaterialEffects'),
    GeometricalPropagator = cms.string('fwdAnalyticalPropagator'),
    Merger = cms.string('CloseComponentsMerger5D'),
    RecoGeometry = cms.string('GlobalDetLayerGeometry'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
