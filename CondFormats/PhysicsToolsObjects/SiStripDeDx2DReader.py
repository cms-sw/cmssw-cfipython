import FWCore.ParameterSet.Config as cms

def SiStripDeDx2DReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx2DReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
