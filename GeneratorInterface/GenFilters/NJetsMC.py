import FWCore.ParameterSet.Config as cms

def NJetsMC(*args, **kwargs):
  mod = cms.EDFilter('NJetsMC',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
