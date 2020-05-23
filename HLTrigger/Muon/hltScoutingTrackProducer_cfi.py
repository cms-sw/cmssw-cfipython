import FWCore.ParameterSet.Config as cms

hltScoutingTrackProducer = cms.EDProducer('HLTScoutingTrackProducer',
  OtherTracks = cms.InputTag('hltPixelTracksL3MuonNoVtx'),
  mightGet = cms.optional.untracked.vstring
)
