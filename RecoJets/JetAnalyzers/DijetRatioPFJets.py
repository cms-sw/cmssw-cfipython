import FWCore.ParameterSet.Config as cms

def DijetRatioPFJets(*args, **kwargs):
  mod = cms.EDAnalyzer('DijetRatioPFJets',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
