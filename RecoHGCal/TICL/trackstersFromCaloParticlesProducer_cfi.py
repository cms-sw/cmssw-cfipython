import FWCore.ParameterSet.Config as cms

trackstersFromCaloParticlesProducer = cms.EDProducer('TrackstersFromCaloParticlesProducer',
  detector = cms.string('HGCAL'),
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  time_layerclusters = cms.InputTag('hgcalLayerClusters', 'timeLayerCluster'),
  filtered_mask = cms.InputTag('filteredLayerClustersSimTracksters', 'ticlSimTracksters'),
  caloparticles = cms.InputTag('mix', 'MergedCaloTruth'),
  associator = cms.InputTag('layerClusterCaloParticleAssociationProducer'),
  fractionCut = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
