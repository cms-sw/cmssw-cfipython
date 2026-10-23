import FWCore.ParameterSet.Config as cms

def TestRandomNumberServiceGlobal(*args, **kwargs):
  mod = cms.EDAnalyzer('TestRandomNumberServiceGlobal',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
