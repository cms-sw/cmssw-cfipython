import FWCore.ParameterSet.Config as cms

def TestBtagPayloads(**kwargs):
  mod = cms.EDAnalyzer('TestBtagPayloads',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
