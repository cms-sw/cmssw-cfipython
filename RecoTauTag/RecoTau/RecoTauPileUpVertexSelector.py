import FWCore.ParameterSet.Config as cms

def RecoTauPileUpVertexSelector(*args, **kwargs):
  mod = cms.EDFilter('RecoTauPileUpVertexSelector',
    minTrackSumPt = cms.required.double,
    src = cms.required.InputTag,
    filter = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
