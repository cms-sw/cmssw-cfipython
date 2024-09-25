import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_HGCalSoALayerClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::HGCalSoALayerClustersProducer',
    hgcalRecHitsLayerClustersSoA = cms.InputTag('TO BE DEFINED'),
    hgcalRecHitsSoA = cms.InputTag('TO BE DEFINED'),
    thresholdW0 = cms.double(2.9),
    positionDeltaRho2 = cms.double(1.69),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
