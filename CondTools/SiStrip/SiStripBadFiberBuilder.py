import FWCore.ParameterSet.Config as cms

def SiStripBadFiberBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadFiberBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
