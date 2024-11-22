import FWCore.ParameterSet.Config as cms

def PtMinPFJetSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
