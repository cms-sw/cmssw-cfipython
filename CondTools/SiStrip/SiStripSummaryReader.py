import FWCore.ParameterSet.Config as cms

def SiStripSummaryReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripSummaryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
