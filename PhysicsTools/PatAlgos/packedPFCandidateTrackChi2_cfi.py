import FWCore.ParameterSet.Config as cms

packedPFCandidateTrackChi2 = cms.EDProducer('PackedCandidateTrackChi2Producer',
  candidates = cms.InputTag('packedPFCandidates'),
  trackCollection = cms.InputTag('generalTracks'),
  doLostTracks = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
