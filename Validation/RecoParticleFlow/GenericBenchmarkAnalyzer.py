import FWCore.ParameterSet.Config as cms

def GenericBenchmarkAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GenericBenchmarkAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
