import FWCore.ParameterSet.Config as cms

def AMPTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('AMPTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
