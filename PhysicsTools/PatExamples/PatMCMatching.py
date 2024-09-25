import FWCore.ParameterSet.Config as cms

def PatMCMatching(*args, **kwargs):
  mod = cms.EDAnalyzer('PatMCMatching',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
