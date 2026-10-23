import FWCore.ParameterSet.Config as cms

def LHCInfoPerLSPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('LHCInfoPerLSPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
