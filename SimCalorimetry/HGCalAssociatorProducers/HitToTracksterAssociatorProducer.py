import FWCore.ParameterSet.Config as cms

def HitToTracksterAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('HitToTracksterAssociatorProducer',
    layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracksters = cms.InputTag('ticlTracksters'),
    hitMapTag = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
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
