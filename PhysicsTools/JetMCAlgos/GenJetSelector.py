import FWCore.ParameterSet.Config as cms

def GenJetSelector(*args, **kwargs):
  mod = cms.EDFilter('GenJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
