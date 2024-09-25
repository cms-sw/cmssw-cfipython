import FWCore.ParameterSet.Config as cms

def PatMCMatchingExtended(*args, **kwargs):
  mod = cms.EDAnalyzer('PatMCMatchingExtended',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
