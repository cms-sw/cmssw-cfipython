import FWCore.ParameterSet.Config as cms

def HitToBarrelTracksterAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('HitToBarrelTracksterAssociatorProducer',
    layer_clusters = cms.InputTag('barrelLayerClusters'),
    tracksters = cms.InputTag('ticlBarrelTracksters'),
    hitMapTag = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.VInputTag(
      'particleFlowRecHitECAL',
      'particleFlowRecHitHBHE'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
