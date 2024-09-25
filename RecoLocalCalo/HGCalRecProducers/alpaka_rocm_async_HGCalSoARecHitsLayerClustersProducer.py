import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HGCalSoARecHitsLayerClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HGCalSoARecHitsLayerClustersProducer',
    hgcalRecHitsSoA = cms.InputTag('TO BE DEFINED'),
    deltac = cms.double(1.3),
    kappa = cms.double(9),
    outlierDeltaFactor = cms.double(2),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
