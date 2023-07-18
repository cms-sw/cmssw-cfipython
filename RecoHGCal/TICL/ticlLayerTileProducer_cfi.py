import FWCore.ParameterSet.Config as cms

ticlLayerTileProducer = cms.EDProducer('TICLLayerTileProducer',
  detector = cms.string('HGCAL'),
  layer_clusters = cms.InputTag('hgcalMergeLayerClusters'),
  layer_HFNose_clusters = cms.InputTag('hgcalLayerClustersHFNose'),
  mightGet = cms.optional.untracked.vstring
)
