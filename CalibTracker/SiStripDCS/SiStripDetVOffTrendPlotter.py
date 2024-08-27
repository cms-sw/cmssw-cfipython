import FWCore.ParameterSet.Config as cms

def SiStripDetVOffTrendPlotter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffTrendPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
