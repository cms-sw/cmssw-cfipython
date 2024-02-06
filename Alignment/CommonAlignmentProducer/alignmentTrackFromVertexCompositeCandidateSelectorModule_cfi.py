import FWCore.ParameterSet.Config as cms

alignmentTrackFromVertexCompositeCandidateSelectorModule = cms.EDFilter('AlignmentTrackFromVertexCompositeCandidateSelectorModule',
  src = cms.InputTag('generalTracks'),
  filter = cms.bool(False),
  vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
  mightGet = cms.optional.untracked.vstring
)
