import FWCore.ParameterSet.Config as cms

trackSelectorByRegion = cms.EDProducer('TrackSelectorByRegion',
  tracks = cms.InputTag('hltPixelTracks'),
  regions = cms.InputTag(''),
  produceTrackCollection = cms.bool(True),
  produceMask = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
