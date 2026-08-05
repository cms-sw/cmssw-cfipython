import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_TICLGeomESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::TICLGeomESProducer',
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
