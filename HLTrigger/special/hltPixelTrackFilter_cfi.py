import FWCore.ParameterSet.Config as cms

hltPixelTrackFilter = cms.EDFilter('HLTPixelTrackFilter',
  pixelTracks = cms.InputTag('hltPixelTracks'),
  minPixelTracks = cms.uint32(0),
  maxPixelTracks = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
