import FWCore.ParameterSet.Config as cms

def ZdcTBAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ZdcTBAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
