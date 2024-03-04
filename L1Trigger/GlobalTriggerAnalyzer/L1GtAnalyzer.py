import FWCore.ParameterSet.Config as cms

def L1GtAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1GtAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
