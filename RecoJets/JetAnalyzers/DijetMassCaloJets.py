import FWCore.ParameterSet.Config as cms

def DijetMassCaloJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetMassCaloJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
