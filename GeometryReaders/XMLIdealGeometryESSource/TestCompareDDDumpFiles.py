import FWCore.ParameterSet.Config as cms

def TestCompareDDDumpFiles(**kwargs):
  mod = cms.EDAnalyzer('TestCompareDDDumpFiles',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
