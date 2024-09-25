import FWCore.ParameterSet.Config as cms

def SCSimpleAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SCSimpleAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
