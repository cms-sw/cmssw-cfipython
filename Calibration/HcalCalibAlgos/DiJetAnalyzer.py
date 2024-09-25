import FWCore.ParameterSet.Config as cms

def DiJetAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DiJetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
