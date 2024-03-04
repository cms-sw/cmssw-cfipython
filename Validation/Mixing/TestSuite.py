import FWCore.ParameterSet.Config as cms

def TestSuite(**kwargs):
  mod = cms.EDAnalyzer('TestSuite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
