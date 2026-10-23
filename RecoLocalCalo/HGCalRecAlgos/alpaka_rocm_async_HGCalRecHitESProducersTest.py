import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HGCalRecHitESProducersTest(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HGCalRecHitESProducersTest',
    indexSource = cms.ESInputTag('', ''),
    configSource = cms.ESInputTag('', ''),
    calibParamSource = cms.ESInputTag('', ''),
    maxchans = cms.int32(500),
    maxmods = cms.int32(8),
    maxfeds = cms.int32(25),
    fedjson = cms.string(''),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
