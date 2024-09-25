import FWCore.ParameterSet.Config as cms

def DumpDBToFile(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpDBToFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
