import FWCore.ParameterSet.Config as cms

def SiStripApvGainDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
