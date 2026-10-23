import FWCore.ParameterSet.Config as cms

def TestCompareDDDumpFiles(*args, **kwargs):
  mod = cms.EDAnalyzer('TestCompareDDDumpFiles',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
