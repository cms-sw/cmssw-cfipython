import FWCore.ParameterSet.Config as cms

def GsfMaterialEffectsESProducer(*args, **kwargs):
  mod = cms.ESProducer('GsfMaterialEffectsESProducer',
    ComponentName = cms.required.string,
    Mass = cms.required.double,
    MultipleScatteringUpdator = cms.required.string,
    EnergyLossUpdator = cms.string('GsfBetheHeitlerUpdator'),
    BetheHeitlerParametrization = cms.required.string,
    BetheHeitlerCorrection = cms.required.int32,
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
