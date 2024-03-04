import FWCore.ParameterSet.Config as cms

def SeedMultiplicityAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SeedMultiplicityAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
