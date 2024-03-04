import FWCore.ParameterSet.Config as cms

def TestMuons(**kwargs):
  mod = cms.EDAnalyzer('TestMuons',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
