import FWCore.ParameterSet.Config as cms

def TestCompareDDSpecsDumpFiles(*args, **kwargs):
  mod = cms.EDAnalyzer('TestCompareDDSpecsDumpFiles',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
