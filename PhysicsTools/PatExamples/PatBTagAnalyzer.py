import FWCore.ParameterSet.Config as cms

def PatBTagAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PatBTagAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
