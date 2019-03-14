import FWCore.ParameterSet.Config as cms

packedCandidateTrackValidator = cms.EDAnalyzer('PackedCandidateTrackValidator',
  tracks = cms.untracked.InputTag('generalTracks'),
  vertices = cms.untracked.InputTag('offlinePrimaryVertices'),
  trackToPackedCandidateAssociation = cms.untracked.InputTag('packedPFCandidates'),
  rootFolder = cms.untracked.string('Tracking/PackedCandidate')
)
