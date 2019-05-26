import FWCore.ParameterSet.Config as cms

filteredLayerClustersProducer = cms.EDProducer('FilteredLayerClustersProducer',
  HGCLayerClusters = cms.InputTag('hgcalLayerClusters'),
  LayerClustersInputMask = cms.InputTag('hgcalLayerClusters', 'InitialLayerClustersMask'),
  iteration_label = cms.string('iterationLabelGoesHere'),
  clusterFilter = cms.string('ClusterFilterByAlgo'),
  algo_number = cms.int32(9),
  max_cluster_size = cms.int32(9999)
)
