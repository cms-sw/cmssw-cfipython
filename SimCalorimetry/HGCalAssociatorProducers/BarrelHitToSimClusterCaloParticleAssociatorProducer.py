import FWCore.ParameterSet.Config as cms

def BarrelHitToSimClusterCaloParticleAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('BarrelHitToSimClusterCaloParticleAssociatorProducer',
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    hitMap = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorPFRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
