import FWCore.ParameterSet.Config as cms

def HGCalSoARecHitsLayerClustersProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('HGCalSoARecHitsLayerClustersProducer@alpaka',
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
