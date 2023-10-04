import FWCore.ParameterSet.Config as cms

siStripMonitorApproximateCluster = cms.EDProducer('SiStripMonitorApproximateCluster',
  compareClusters = cms.bool(False),
  ApproxClustersProducer = cms.InputTag('hltSiStripClusters2ApproxClusters'),
  SiStripFEDErrorVector = cms.InputTag('hltSiStripRawToDigi'),
  ClustersProducer = cms.InputTag('hltSiStripClusterizerForRawPrime'),
  folder = cms.string('SiStripApproximateClusters'),
  mightGet = cms.optional.untracked.vstring
)
