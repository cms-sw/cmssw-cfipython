import FWCore.ParameterSet.Config as cms

def GenJetRefSelector(*args, **kwargs):
  mod = cms.EDFilter('GenJetRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
