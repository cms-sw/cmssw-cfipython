import FWCore.ParameterSet.Config as cms

siStripMonitorApproximateCluster = cms.EDProducer('SiStripMonitorApproximateCluster',
  compareClusters = cms.bool(False),
  ApproxClustersProducer = cms.InputTag('hltSiStripClusters2ApproxClusters'),
  ClustersProducer = cms.InputTag('siStripClusters'),
  folder = cms.string('SiStripApproximateClusters'),
  mightGet = cms.optional.untracked.vstring
)
