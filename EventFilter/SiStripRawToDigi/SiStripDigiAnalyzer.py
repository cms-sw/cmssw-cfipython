import FWCore.ParameterSet.Config as cms

def SiStripDigiAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('SiStripDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
