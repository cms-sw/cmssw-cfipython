import FWCore.ParameterSet.Config as cms

def AllHitToTracksterAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllHitToTracksterAssociatorsProducer',
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersCLUE3DHigh',
      'ticlTrackstersLinks',
      'ticlCandidate'
    ),
    hitMapTag = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorHGCRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
