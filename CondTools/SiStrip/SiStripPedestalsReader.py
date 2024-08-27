import FWCore.ParameterSet.Config as cms

def SiStripPedestalsReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripPedestalsReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
