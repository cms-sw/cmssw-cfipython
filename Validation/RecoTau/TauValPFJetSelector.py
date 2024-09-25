import FWCore.ParameterSet.Config as cms

def TauValPFJetSelector(*args, **kwargs):
  mod = cms.EDFilter('TauValPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
