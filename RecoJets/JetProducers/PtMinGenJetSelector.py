import FWCore.ParameterSet.Config as cms

def PtMinGenJetSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinGenJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
