import FWCore.ParameterSet.Config as cms

def RunLumiESAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunLumiESAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
