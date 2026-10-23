import FWCore.ParameterSet.Config as cms

def MagFieldConfigDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('MagFieldConfigDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
