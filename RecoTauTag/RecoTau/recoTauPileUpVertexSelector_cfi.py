import FWCore.ParameterSet.Config as cms

recoTauPileUpVertexSelector = cms.EDFilter('RecoTauPileUpVertexSelector',
  minTrackSumPt = cms.required.double,
  src = cms.required.InputTag,
  filter = cms.required.bool,
  mightGet = cms.optional.untracked.vstring
)
