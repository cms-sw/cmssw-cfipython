import FWCore.ParameterSet.Config as cms

def CaloNavigationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloNavigationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
