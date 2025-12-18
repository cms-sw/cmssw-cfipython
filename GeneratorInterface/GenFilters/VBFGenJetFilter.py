import FWCore.ParameterSet.Config as cms

def VBFGenJetFilter(*args, **kwargs):
  mod = cms.EDFilter('VBFGenJetFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
