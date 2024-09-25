import FWCore.ParameterSet.Config as cms

def PileupJetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PileupJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
