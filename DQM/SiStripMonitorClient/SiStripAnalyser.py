import FWCore.ParameterSet.Config as cms

def SiStripAnalyser(**kwargs):
  mod = cms.EDAnalyzer('SiStripAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
