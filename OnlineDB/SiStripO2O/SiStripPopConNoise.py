import FWCore.ParameterSet.Config as cms

def SiStripPopConNoise(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
