import FWCore.ParameterSet.Config as cms

def DumpScObjects(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpScObjects',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
