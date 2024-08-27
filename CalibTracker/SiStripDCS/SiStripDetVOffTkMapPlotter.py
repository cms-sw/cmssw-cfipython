import FWCore.ParameterSet.Config as cms

def SiStripDetVOffTkMapPlotter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffTkMapPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
