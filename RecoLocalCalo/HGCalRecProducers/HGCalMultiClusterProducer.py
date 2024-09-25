import FWCore.ParameterSet.Config as cms

def HGCalMultiClusterProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalMultiClusterProducer',
    HGCLayerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    verbosity = cms.untracked.uint32(3),
    doSharing = cms.bool(False),
    HGCEEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    HGCFHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    multiclusterRadii = cms.vdouble(
      2,
      5,
      5
    ),
    HGCBHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    HGCLayerClustersSharing = cms.InputTag('hgcalMergeLayerClusters', 'sharing'),
    minClusters = cms.uint32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
