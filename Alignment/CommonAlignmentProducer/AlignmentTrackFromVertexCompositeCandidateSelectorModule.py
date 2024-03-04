import FWCore.ParameterSet.Config as cms

def AlignmentTrackFromVertexCompositeCandidateSelectorModule(**kwargs):
  mod = cms.EDFilter('AlignmentTrackFromVertexCompositeCandidateSelectorModule',
    src = cms.InputTag('generalTracks'),
    filter = cms.bool(False),
    vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
