import FWCore.ParameterSet.Config as cms

def SiStripDaqInfo(**kwargs):
  mod = cms.EDAnalyzer('SiStripDaqInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
