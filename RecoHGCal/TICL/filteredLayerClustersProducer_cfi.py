import FWCore.ParameterSet.Config as cms

filteredLayerClustersProducer = cms.EDProducer('FilteredLayerClustersProducer',
  HGCLayerClusters = cms.InputTag('hgcalLayerClusters'),
  LayerClustersInputMask = cms.InputTag('hgcalLayerClusters', 'InitialLayerClustersMask'),
  iteration_label = cms.string('iterationLabelGoesHere'),
  clusterFilter = cms.string('ClusterFilterByAlgoAndSize'),
  algo_number = cms.int32(9),
  min_cluster_size = cms.int32(0),
  max_cluster_size = cms.int32(9999),
  mightGet = cms.optional.untracked.vstring
)
