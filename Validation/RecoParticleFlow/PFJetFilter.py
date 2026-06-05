import FWCore.ParameterSet.Config as cms

def PFJetFilter(*args, **kwargs):
  mod = cms.EDFilter('PFJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
