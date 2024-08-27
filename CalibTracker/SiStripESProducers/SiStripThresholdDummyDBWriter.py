import FWCore.ParameterSet.Config as cms

def SiStripThresholdDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripThresholdDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
