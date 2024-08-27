import FWCore.ParameterSet.Config as cms

def SiStripDeDx3DReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx3DReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
