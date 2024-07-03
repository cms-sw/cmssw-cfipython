import FWCore.ParameterSet.Config as cms

def HGCalSoALayerClustersProducer_alpaka(**kwargs):
  mod = cms.EDProducer('HGCalSoALayerClustersProducer@alpaka',
    hgcalRecHitsLayerClustersSoA = cms.InputTag('TO BE DEFINED'),
    hgcalRecHitsSoA = cms.InputTag('TO BE DEFINED'),
    thresholdW0 = cms.double(2.9),
    positionDeltaRho2 = cms.double(1.69),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
