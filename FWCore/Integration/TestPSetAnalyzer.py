import FWCore.ParameterSet.Config as cms

def TestPSetAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestPSetAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
