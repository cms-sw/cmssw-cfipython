import FWCore.ParameterSet.Config as cms

def JetIDFailureFilter(*args, **kwargs):
  mod = cms.EDFilter('JetIDFailureFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
