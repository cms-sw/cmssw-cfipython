import FWCore.ParameterSet.Config as cms

trackstersProducer = cms.EDProducer('TrackstersProducer',
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  filtered_mask = cms.InputTag('FilteredLayerClusters', 'iterationLabelGoesHere'),
  original_mask = cms.InputTag('hgcalLayerClusters', 'InitialLayerClustersMask'),
  algo_verbosity = cms.int32(0),
  min_cos_theta = cms.double(0.915),
  min_cos_pointing = cms.double(-1),
  missing_layers = cms.int32(0),
  min_clusters_per_ntuplet = cms.int32(10),
  mightGet = cms.optional.untracked.vstring
)
