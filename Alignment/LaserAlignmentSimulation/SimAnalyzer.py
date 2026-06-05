import FWCore.ParameterSet.Config as cms

def SimAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SimAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
