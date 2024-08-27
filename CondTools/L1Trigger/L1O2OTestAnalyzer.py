import FWCore.ParameterSet.Config as cms

def L1O2OTestAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1O2OTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
