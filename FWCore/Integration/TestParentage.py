import FWCore.ParameterSet.Config as cms

def TestParentage(**kwargs):
  mod = cms.EDAnalyzer('TestParentage',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
