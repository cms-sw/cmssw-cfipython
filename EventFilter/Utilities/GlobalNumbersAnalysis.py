import FWCore.ParameterSet.Config as cms

def GlobalNumbersAnalysis(*args, **kwargs):
  mod = cms.EDAnalyzer('GlobalNumbersAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
