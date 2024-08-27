import FWCore.ParameterSet.Config as cms

def CompareGeneratorResultsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CompareGeneratorResultsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
