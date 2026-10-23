import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_LSTModulesDevESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::LSTModulesDevESProducer',
    ptCutLabel = cms.string('0.8'),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
