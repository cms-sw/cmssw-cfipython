import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_HGCalSoARecHitsLayerClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::HGCalSoARecHitsLayerClustersProducer',
    hgcalRecHitsSoA = cms.InputTag('TO BE DEFINED'),
    deltac = cms.float(1.3),
    kappa = cms.float(9),
    outlierDeltaFactor = cms.float(2),
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
