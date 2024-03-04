import FWCore.ParameterSet.Config as cms

def TestESDummyDataAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestESDummyDataAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
