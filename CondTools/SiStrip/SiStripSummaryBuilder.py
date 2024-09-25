import FWCore.ParameterSet.Config as cms

def SiStripSummaryBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripSummaryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
