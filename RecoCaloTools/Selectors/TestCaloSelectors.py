import FWCore.ParameterSet.Config as cms

def TestCaloSelectors(**kwargs):
  mod = cms.EDAnalyzer('TestCaloSelectors',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
