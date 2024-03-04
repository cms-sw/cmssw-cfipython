import FWCore.ParameterSet.Config as cms

def SiStripGainReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
