import FWCore.ParameterSet.Config as cms

def SiStripSpyDisplayModule(**kwargs):
  mod = cms.EDAnalyzer('SiStripSpyDisplayModule',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
