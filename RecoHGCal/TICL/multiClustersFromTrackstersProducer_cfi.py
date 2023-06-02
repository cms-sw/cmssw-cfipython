import FWCore.ParameterSet.Config as cms

multiClustersFromTrackstersProducer = cms.EDProducer('MultiClustersFromTrackstersProducer',
  Tracksters = cms.InputTag('Tracksters', 'TrackstersByCA'),
  LayerClusters = cms.InputTag('hgcalMergeLayerClusters'),
  verbosity = cms.untracked.uint32(3),
  mightGet = cms.optional.untracked.vstring
)
