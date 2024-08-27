import FWCore.ParameterSet.Config as cms

def SiStripBadStripDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
