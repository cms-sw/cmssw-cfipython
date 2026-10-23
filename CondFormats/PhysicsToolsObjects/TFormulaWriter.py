import FWCore.ParameterSet.Config as cms

def TFormulaWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('TFormulaWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
