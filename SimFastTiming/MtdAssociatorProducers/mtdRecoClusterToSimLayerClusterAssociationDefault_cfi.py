import FWCore.ParameterSet.Config as cms

mtdRecoClusterToSimLayerClusterAssociationDefault = cms.EDProducer('MtdRecoClusterToSimLayerClusterAssociatorEDProducer',
  associator = cms.InputTag('mtdRecoClusterToSimLayerClusterAssociatorByHits'),
  mtdSimClustersTag = cms.InputTag('mix', 'MergedMtdTruthLC'),
  btlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLBarrel'),
  etlRecoClustersTag = cms.InputTag('mtdClusters', 'FTLEndcap'),
  mightGet = cms.optional.untracked.vstring
)
