import FWCore.ParameterSet.Config as cms

def PatBJetTagAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatBJetTagAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
