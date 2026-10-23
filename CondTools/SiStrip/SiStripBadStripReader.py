import FWCore.ParameterSet.Config as cms

def SiStripBadStripReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
