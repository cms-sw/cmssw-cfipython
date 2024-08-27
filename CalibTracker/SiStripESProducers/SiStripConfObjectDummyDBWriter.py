import FWCore.ParameterSet.Config as cms

def SiStripConfObjectDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripConfObjectDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
