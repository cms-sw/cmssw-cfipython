import FWCore.ParameterSet.Config as cms

v0EventSelector = cms.EDFilter('V0EventSelector',
  vertexCompositeCandidates = cms.InputTag('generalV0Candidates', 'Kshort'),
  minCandidates = cms.uint32(1),
  mightGet = cms.optional.untracked.vstring
)
