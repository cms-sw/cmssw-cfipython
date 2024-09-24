import FWCore.ParameterSet.Config as cms

def FilteredLayerClustersProducer(*args, **kwargs):
  mod = cms.EDProducer('FilteredLayerClustersProducer',
    LayerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    LayerClustersInputMask = cms.InputTag('hgcalMergeLayerClusters', 'InitialLayerClustersMask'),
    iteration_label = cms.string('iterationLabelGoesHere'),
    clusterFilter = cms.string('ClusterFilterByAlgoAndSize'),
    algo_number = cms.vint32(
      6,
      7,
      8
    ),
    min_cluster_size = cms.int32(0),
    max_cluster_size = cms.int32(9999),
    min_layerId = cms.int32(0),
    max_layerId = cms.int32(9999),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
