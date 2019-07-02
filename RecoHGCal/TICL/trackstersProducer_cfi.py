import FWCore.ParameterSet.Config as cms

trackstersProducer = cms.EDProducer('TrackstersProducer',
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  filtered_mask = cms.InputTag('FilteredLayerClusters', 'iterationLabelGoesHere'),
  original_mask = cms.InputTag('hgcalLayerClusters', 'InitialLayerClustersMask'),
  time_layerclusters = cms.InputTag('hgcalLayerClusters', 'timeLayerCluster'),
  layer_clusters_tiles = cms.InputTag('TICLLayerTileProducer'),
  algo_verbosity = cms.int32(0),
  min_cos_theta = cms.double(0.915),
  min_cos_pointing = cms.double(-1),
  missing_layers = cms.int32(0),
  min_clusters_per_ntuplet = cms.int32(10),
  max_delta_time = cms.double(0.09),
  mightGet = cms.optional.untracked.vstring
)
