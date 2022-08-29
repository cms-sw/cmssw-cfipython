import FWCore.ParameterSet.Config as cms

simMuonGEMPadDigiClustersDef = cms.EDProducer('GEMPadDigiClusterProducer',
  InputCollection = cms.InputTag('simMuonGEMPadDigis'),
  nPartitionsGE11 = cms.uint32(4),
  nPartitionsGE21 = cms.uint32(4),
  maxClustersPartitionGE11 = cms.uint32(4),
  maxClustersPartitionGE21 = cms.uint32(4),
  nOHGE11 = cms.uint32(1),
  nOHGE21 = cms.uint32(4),
  maxClustersOHGE11 = cms.uint32(8),
  maxClustersOHGE21 = cms.uint32(8),
  maxClusterSize = cms.uint32(8),
  sendOverflowClusters = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
