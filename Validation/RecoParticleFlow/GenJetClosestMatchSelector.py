import FWCore.ParameterSet.Config as cms

def GenJetClosestMatchSelector(*args, **kwargs):
  mod = cms.EDFilter('GenJetClosestMatchSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
