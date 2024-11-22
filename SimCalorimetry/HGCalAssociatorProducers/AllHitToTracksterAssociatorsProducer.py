import FWCore.ParameterSet.Config as cms

def AllHitToTracksterAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllHitToTracksterAssociatorsProducer',
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersCLUE3DHigh',
      'ticlTrackstersLinks',
      'ticlCandidate'
    ),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
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
