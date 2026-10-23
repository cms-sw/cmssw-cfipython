import FWCore.ParameterSet.Config as cms

def TestGenTtbarCategories(*args, **kwargs):
  mod = cms.EDAnalyzer('TestGenTtbarCategories',
    genTtbarId = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
