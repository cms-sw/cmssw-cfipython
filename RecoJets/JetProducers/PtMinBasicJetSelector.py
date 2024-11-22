import FWCore.ParameterSet.Config as cms

def PtMinBasicJetSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinBasicJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
