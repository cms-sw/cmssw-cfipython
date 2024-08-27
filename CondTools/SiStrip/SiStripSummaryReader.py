import FWCore.ParameterSet.Config as cms

def SiStripSummaryReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripSummaryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
