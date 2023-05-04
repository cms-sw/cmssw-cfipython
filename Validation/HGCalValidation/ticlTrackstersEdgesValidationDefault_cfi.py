import FWCore.ParameterSet.Config as cms

ticlTrackstersEdgesValidationDefault = cms.EDProducer('TICLTrackstersEdgesValidation',
  tracksterCollections = cms.VInputTag(
    'ticlTrackstersTrk',
    'ticlTrackstersTrkEM',
    'ticlTrackstersEM',
    'ticlTrackstersHAD',
    'ticlTrackstersMerge'
  ),
  layerClusters = cms.InputTag('hgcalLayerClusters'),
  ticlSeedingGlobal = cms.InputTag('ticlSeedingGlobal'),
  ticlSeedingTrk = cms.InputTag('ticlSeedingTrk'),
  folder = cms.string('HGCAL/'),
  mightGet = cms.optional.untracked.vstring
)
