import FWCore.ParameterSet.Config as cms

def HGCalSoARecHitsLayerClustersProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('HGCalSoARecHitsLayerClustersProducer@alpaka',
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
