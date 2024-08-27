import FWCore.ParameterSet.Config as cms

def TestCompareDDSpecsDumpFiles(**kwargs):
  mod = cms.EDAnalyzer('TestCompareDDSpecsDumpFiles',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
