import FWCore.ParameterSet.Config as cms

packedCandidateTrackValidator = cms.EDAnalyzer('PackedCandidateTrackValidator',
  tracks = cms.untracked.InputTag('generalTracks'),
  trackToPackedCandiadteAssociation = cms.untracked.InputTag('packedPFCandidates'),
  rootFolder = cms.untracked.string('Tracking/PackedCandidate')
)
