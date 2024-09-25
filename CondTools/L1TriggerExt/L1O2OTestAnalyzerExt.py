import FWCore.ParameterSet.Config as cms

def L1O2OTestAnalyzerExt(*args, **kwargs):
  mod = cms.EDAnalyzer('L1O2OTestAnalyzerExt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
