import FWCore.ParameterSet.Config as cms

trackstersFromSimClustersProducer = cms.EDProducer('TrackstersFromSimClustersProducer',
  detector = cms.string('HGCAL'),
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  time_layerclusters = cms.InputTag('hgcalLayerClusters', 'timeLayerCluster'),
  filtered_mask = cms.InputTag('filteredLayerClustersSimTracksters', 'ticlSimTracksters'),
  simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
  caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
  layerClusterSimClusterAssociator = cms.untracked.InputTag('layerClusterSimClusterAssociationProducer'),
  layerClusterCaloParticleAssociator = cms.untracked.InputTag('layerClusterCaloParticleAssociationProducer'),
  fractionCut = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
