import FWCore.ParameterSet.Config as cms

ticlCandidateFromTrackstersProducer = cms.EDProducer('TICLCandidateFromTrackstersProducer',
  tracksterCollections = cms.VInputTag(
    'trackstersTrk',
    'trackstersMIP',
    'trackstersEM',
    'trackstersHAD'
  ),
  minParticleProbability = cms.double(0),
  momentumPlugin = cms.PSet(
    plugin = cms.string('TracksterP4FromEnergySum'),
    energyFromRegression = cms.bool(False),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    layerClusters = cms.InputTag('hgcalMergeLayerClusters'),
    tracks = cms.InputTag('generalTracks')
  ),
  trackPlugin = cms.PSet(
    plugin = cms.string('TracksterRecoTrackPlugin')
  ),
  mightGet = cms.optional.untracked.vstring
)
