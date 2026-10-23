import FWCore.ParameterSet.Config as cms

def DeleteEarlyRefProdReader(*args, **kwargs):
  mod = cms.EDAnalyzer('DeleteEarlyRefProdReader',
    tag = cms.required.untracked.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
