import FWCore.ParameterSet.Config as cms

def HGCalSoARecHitsLayerClustersProducer_alpaka(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
