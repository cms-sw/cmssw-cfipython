import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_TICLGeomESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::TICLGeomESProducer',
    detectors = cms.vstring('HGCal'),
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
