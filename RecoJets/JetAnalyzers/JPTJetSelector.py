import FWCore.ParameterSet.Config as cms

def JPTJetSelector(*args, **kwargs):
  mod = cms.EDFilter('JPTJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
