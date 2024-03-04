import FWCore.ParameterSet.Config as cms

def SiStripDcsInfo(**kwargs):
  mod = cms.EDAnalyzer('SiStripDcsInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
