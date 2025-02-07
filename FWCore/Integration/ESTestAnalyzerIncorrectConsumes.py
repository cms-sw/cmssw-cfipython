import FWCore.ParameterSet.Config as cms

def ESTestAnalyzerIncorrectConsumes(*args, **kwargs):
  mod = cms.EDAnalyzer('ESTestAnalyzerIncorrectConsumes',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
