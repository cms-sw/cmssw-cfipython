import FWCore.ParameterSet.Config as cms

def SiStripNoisesDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
