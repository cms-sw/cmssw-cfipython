import FWCore.ParameterSet.Config as cms

def TestConverter2(**kwargs):
  mod = cms.EDAnalyzer('TestConverter2',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
