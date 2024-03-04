import FWCore.ParameterSet.Config as cms

def TestPortableAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestPortableAnalyzer',
    source = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
