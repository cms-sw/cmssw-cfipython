import FWCore.ParameterSet.Config as cms

def SiStripDeDx2DBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx2DBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
