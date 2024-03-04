import FWCore.ParameterSet.Config as cms

def SiStripBadStripReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
