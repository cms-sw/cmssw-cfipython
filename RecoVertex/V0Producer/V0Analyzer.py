import FWCore.ParameterSet.Config as cms

def V0Analyzer(**kwargs):
  mod = cms.EDAnalyzer('V0Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
