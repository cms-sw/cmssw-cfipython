import FWCore.ParameterSet.Config as cms

def DijetRatioGenJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetRatioGenJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
