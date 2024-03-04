import FWCore.ParameterSet.Config as cms

def L1MuGMTTree(**kwargs):
  mod = cms.EDAnalyzer('L1MuGMTTree',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
