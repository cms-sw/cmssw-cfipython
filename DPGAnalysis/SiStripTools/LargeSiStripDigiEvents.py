import FWCore.ParameterSet.Config as cms

def LargeSiStripDigiEvents(**kwargs):
  mod = cms.EDFilter('LargeSiStripDigiEvents',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
