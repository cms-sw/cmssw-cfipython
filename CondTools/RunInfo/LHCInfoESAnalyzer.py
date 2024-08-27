import FWCore.ParameterSet.Config as cms

def LHCInfoESAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LHCInfoESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
