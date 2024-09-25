import FWCore.ParameterSet.Config as cms

def ResolutionAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ResolutionAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
