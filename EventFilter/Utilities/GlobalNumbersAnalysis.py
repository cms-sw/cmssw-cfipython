import FWCore.ParameterSet.Config as cms

def GlobalNumbersAnalysis(**kwargs):
  mod = cms.EDAnalyzer('GlobalNumbersAnalysis',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
