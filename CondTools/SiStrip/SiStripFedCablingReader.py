import FWCore.ParameterSet.Config as cms

def SiStripFedCablingReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
