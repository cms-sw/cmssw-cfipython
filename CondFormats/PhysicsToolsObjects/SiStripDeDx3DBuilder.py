import FWCore.ParameterSet.Config as cms

def SiStripDeDx3DBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx3DBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
