import FWCore.ParameterSet.Config as cms

def SiStripSummaryBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripSummaryBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
