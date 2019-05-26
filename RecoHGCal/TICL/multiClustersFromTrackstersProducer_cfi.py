import FWCore.ParameterSet.Config as cms

multiClustersFromTrackstersProducer = cms.EDProducer('MultiClustersFromTrackstersProducer',
  Tracksters = cms.InputTag('Tracksters', 'TrackstersByCA'),
  LayerClusters = cms.InputTag('hgcalLayerClusters'),
  label = cms.string('MultiClustersFromTracksterByCA'),
  verbosity = cms.untracked.uint32(3)
)
