import FWCore.ParameterSet.Config as cms

simTrackstersProducer = cms.EDProducer('SimTrackstersProducer',
  detector = cms.string('HGCAL'),
  layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
  time_layerclusters = cms.InputTag('hgcalMergeLayerClusters', 'timeLayerCluster'),
  filtered_mask = cms.InputTag('filteredLayerClustersSimTracksters', 'ticlSimTracksters'),
  simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
  caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
  layerClusterSimClusterAssociator = cms.InputTag('layerClusterSimClusterAssociationProducer'),
  layerClusterCaloParticleAssociator = cms.InputTag('layerClusterCaloParticleAssociationProducer'),
  fractionCut = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
