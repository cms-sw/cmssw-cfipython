import FWCore.ParameterSet.Config as cms

def AlignmentTrackFromVertexCompositeCandidateSelectorModule(*args, **kwargs):
  mod = cms.EDFilter('AlignmentTrackFromVertexCompositeCandidateSelectorModule',
    src = cms.InputTag('generalTracks'),
    filter = cms.bool(False),
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
