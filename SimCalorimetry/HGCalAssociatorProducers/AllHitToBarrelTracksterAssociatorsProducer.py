import FWCore.ParameterSet.Config as cms

def AllHitToBarrelTracksterAssociatorsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllHitToBarrelTracksterAssociatorsProducer',
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracksterCollections = cms.VInputTag('ticlTrackstersCLUE3DBarrel'),
    hitMapTag = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorPFRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
