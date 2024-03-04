import FWCore.ParameterSet.Config as cms

def HGCalMultiClusterProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
