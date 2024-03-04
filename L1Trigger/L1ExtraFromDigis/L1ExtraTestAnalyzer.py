import FWCore.ParameterSet.Config as cms

def L1ExtraTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1ExtraTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
