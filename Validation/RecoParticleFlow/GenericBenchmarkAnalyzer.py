import FWCore.ParameterSet.Config as cms

def GenericBenchmarkAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GenericBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
