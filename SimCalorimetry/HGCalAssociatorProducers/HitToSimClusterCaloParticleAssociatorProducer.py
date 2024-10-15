import FWCore.ParameterSet.Config as cms

def HitToSimClusterCaloParticleAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('HitToSimClusterCaloParticleAssociatorProducer',
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    simClusters = cms.InputTag('mix', 'MergedCaloTruth'),
    hitMap = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
    hits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
