import FWCore.ParameterSet.Config as cms

def L1GtDataEmulAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1GtDataEmulAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
