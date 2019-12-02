import FWCore.ParameterSet.Config as cms

ticlLayerTileProducer = cms.EDProducer('TICLLayerTileProducer',
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  mightGet = cms.optional.untracked.vstring
)
