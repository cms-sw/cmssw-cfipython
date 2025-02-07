import FWCore.ParameterSet.Config as cms

def PatZToMuMuAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatZToMuMuAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
