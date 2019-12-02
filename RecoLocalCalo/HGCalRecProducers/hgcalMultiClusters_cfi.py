import FWCore.ParameterSet.Config as cms

hgcalMultiClusters = cms.EDProducer('HGCalMultiClusterProducer',
  HGCLayerClusters = cms.InputTag('hgcalLayerClusters'),
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
  HGCLayerClustersSharing = cms.InputTag('hgcalLayerClusters', 'sharing'),
  minClusters = cms.uint32(3),
  mightGet = cms.optional.untracked.vstring
)
