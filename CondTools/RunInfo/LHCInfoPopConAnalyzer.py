import FWCore.ParameterSet.Config as cms

def LHCInfoPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
