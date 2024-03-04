import FWCore.ParameterSet.Config as cms

def SiStripNoisesReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
