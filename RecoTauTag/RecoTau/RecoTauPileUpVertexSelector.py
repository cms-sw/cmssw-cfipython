import FWCore.ParameterSet.Config as cms

def RecoTauPileUpVertexSelector(**kwargs):
  mod = cms.EDFilter('RecoTauPileUpVertexSelector',
    minTrackSumPt = cms.required.double,
    src = cms.required.InputTag,
    filter = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
