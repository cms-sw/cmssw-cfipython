import FWCore.ParameterSet.Config as cms

def GenFilterEfficiencyAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GenFilterEfficiencyAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
