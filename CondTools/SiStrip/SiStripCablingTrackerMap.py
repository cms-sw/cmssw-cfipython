import FWCore.ParameterSet.Config as cms

def SiStripCablingTrackerMap(**kwargs):
  mod = cms.EDAnalyzer('SiStripCablingTrackerMap',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
