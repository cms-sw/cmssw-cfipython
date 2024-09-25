import FWCore.ParameterSet.Config as cms

def LargeSiStripDigiEvents(*args, **kwargs):
  mod = cms.EDFilter('LargeSiStripDigiEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
