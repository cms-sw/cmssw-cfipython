import FWCore.ParameterSet.Config as cms

def DumpGctDigis(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpGctDigis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
