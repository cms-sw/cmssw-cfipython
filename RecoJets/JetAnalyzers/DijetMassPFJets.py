import FWCore.ParameterSet.Config as cms

def DijetMassPFJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetMassPFJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
