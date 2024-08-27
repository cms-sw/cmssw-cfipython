import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerL(**kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerL',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
