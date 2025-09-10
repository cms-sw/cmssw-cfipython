import FWCore.ParameterSet.Config as cms

def SiStripSpyIdentifyRuns(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripSpyIdentifyRuns',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
