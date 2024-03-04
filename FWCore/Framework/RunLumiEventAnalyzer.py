import FWCore.ParameterSet.Config as cms

def RunLumiEventAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('RunLumiEventAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
