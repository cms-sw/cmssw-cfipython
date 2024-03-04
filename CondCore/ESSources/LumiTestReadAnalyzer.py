import FWCore.ParameterSet.Config as cms

def LumiTestReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('LumiTestReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
