import FWCore.ParameterSet.Config as cms

def SiStripSpyIdentifyRuns(**kwargs):
  mod = cms.EDAnalyzer('SiStripSpyIdentifyRuns',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
