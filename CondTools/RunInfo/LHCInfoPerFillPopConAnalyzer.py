import FWCore.ParameterSet.Config as cms

def LHCInfoPerFillPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerFillPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
