import FWCore.ParameterSet.Config as cms

def edmtest_IntFromRunConsumingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::IntFromRunConsumingAnalyzer',
    getFromModule = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
