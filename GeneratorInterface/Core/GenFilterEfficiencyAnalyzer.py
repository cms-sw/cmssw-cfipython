import FWCore.ParameterSet.Config as cms

def GenFilterEfficiencyAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GenFilterEfficiencyAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
