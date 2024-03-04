import FWCore.ParameterSet.Config as cms

def LumiBasedUpdateAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LumiBasedUpdateAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
