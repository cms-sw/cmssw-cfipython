import FWCore.ParameterSet.Config as cms

def validateBTagDB(*args, **kwargs):
  mod = cms.EDAnalyzer('validateBTagDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
