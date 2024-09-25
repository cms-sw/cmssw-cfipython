import FWCore.ParameterSet.Config as cms

def RunLumiEventAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('RunLumiEventAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
