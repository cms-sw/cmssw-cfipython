import FWCore.ParameterSet.Config as cms

def SiStripSpyExtractRunModule(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripSpyExtractRunModule',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
