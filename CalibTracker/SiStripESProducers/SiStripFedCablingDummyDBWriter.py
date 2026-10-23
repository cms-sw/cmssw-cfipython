import FWCore.ParameterSet.Config as cms

def SiStripFedCablingDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripFedCablingDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
