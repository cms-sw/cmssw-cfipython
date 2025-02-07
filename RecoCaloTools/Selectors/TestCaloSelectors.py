import FWCore.ParameterSet.Config as cms

def TestCaloSelectors(*args, **kwargs):
  mod = cms.EDAnalyzer('TestCaloSelectors',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
