import FWCore.ParameterSet.Config as cms

def SiStripSpyExtractRunModule(**kwargs):
  mod = cms.EDAnalyzer('SiStripSpyExtractRunModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
