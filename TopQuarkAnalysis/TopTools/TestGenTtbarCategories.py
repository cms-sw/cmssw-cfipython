import FWCore.ParameterSet.Config as cms

def TestGenTtbarCategories(**kwargs):
  mod = cms.EDAnalyzer('TestGenTtbarCategories',
    genTtbarId = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
