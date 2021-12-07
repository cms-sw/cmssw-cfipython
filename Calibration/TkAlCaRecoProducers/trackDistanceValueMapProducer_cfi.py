import FWCore.ParameterSet.Config as cms

trackDistanceValueMapProducer = cms.EDProducer('TrackDistanceValueMapProducer',
  muonTracks = cms.InputTag('ALCARECOSiPixelCalSingleMuonTight'),
  allTracks = cms.InputTag('generalTracks'),
  saveUpToNthClosest = cms.uint32(1),
  mightGet = cms.optional.untracked.vstring
)
