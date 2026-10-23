import FWCore.ParameterSet.Config as cms

def V0Analyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('V0Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
