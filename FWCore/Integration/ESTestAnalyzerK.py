import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerK(**kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerK',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
