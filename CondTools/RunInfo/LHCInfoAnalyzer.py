import FWCore.ParameterSet.Config as cms

def LHCInfoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
