import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerIncorrectConsumes(**kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerIncorrectConsumes',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
