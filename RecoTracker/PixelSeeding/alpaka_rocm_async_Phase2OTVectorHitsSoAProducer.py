import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_Phase2OTVectorHitsSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::Phase2OTVectorHitsSoAProducer',
    otRecHitsSoA = cms.InputTag('caOTRecHitsSoA'),
    maxWidthBarrelFlat = cms.vdouble(
      0,
      0.0575,
      0.06,
      0.08,
      0.09,
      0.12,
      0.2
    ),
    maxWidthBarrelTilted = cms.vdouble(
      0,
      0.0575,
      0.06,
      0.08,
      0.09,
      0.12,
      0.2
    ),
    maxWidthEndcap = cms.vdouble(
      0,
      0.1,
      0.1,
      0.1,
      0.1,
      0.1
    ),
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
