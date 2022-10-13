import FWCore.ParameterSet.Config as cms

isFromLostTrackMapProducer = cms.EDProducer('IsFromLostTrackMapProducer',
  srcIsoTracks = cms.required.InputTag,
  lostTracks = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
