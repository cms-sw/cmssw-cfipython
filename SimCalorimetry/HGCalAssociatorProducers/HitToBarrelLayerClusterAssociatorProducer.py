import FWCore.ParameterSet.Config as cms

def HitToBarrelLayerClusterAssociatorProducer(*args, **kwargs):
  mod = cms.EDProducer('HitToBarrelLayerClusterAssociatorProducer',
    layer_clusters = cms.InputTag('barrelLayerClusters'),
    hitMap = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
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
