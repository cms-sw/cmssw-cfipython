import FWCore.ParameterSet.Config as cms

def testChannel(**kwargs):
  mod = cms.EDAnalyzer('testChannel',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
