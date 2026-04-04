import FWCore.ParameterSet.Config as cms

def QualityCutsAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('QualityCutsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
