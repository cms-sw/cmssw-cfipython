import FWCore.ParameterSet.Config as cms

def SiStripBaselineAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBaselineAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
