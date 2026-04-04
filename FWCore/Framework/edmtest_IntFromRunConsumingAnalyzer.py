import FWCore.ParameterSet.Config as cms

def edmtest_IntFromRunConsumingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::IntFromRunConsumingAnalyzer',
    getFromModule = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
