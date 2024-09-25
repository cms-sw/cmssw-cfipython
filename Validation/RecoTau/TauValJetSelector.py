import FWCore.ParameterSet.Config as cms

def TauValJetSelector(*args, **kwargs):
  mod = cms.EDFilter('TauValJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
