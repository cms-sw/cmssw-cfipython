import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HGCalRecHitESProducersTest(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HGCalRecHitESProducersTest',
    indexSource = cms.ESInputTag('', ''),
    configSource = cms.ESInputTag('', ''),
    configParamSource = cms.ESInputTag('', ''),
    calibParamSource = cms.ESInputTag('', ''),
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
