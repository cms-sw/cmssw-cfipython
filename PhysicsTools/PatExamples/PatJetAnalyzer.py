import FWCore.ParameterSet.Config as cms

def PatJetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
