import FWCore.ParameterSet.Config as cms

def HitToLayerClusterAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('HitToLayerClusterAssociatorProducer',
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
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
