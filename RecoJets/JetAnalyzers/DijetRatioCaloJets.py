import FWCore.ParameterSet.Config as cms

def DijetRatioCaloJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetRatioCaloJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
