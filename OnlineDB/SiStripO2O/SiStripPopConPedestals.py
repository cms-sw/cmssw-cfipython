import FWCore.ParameterSet.Config as cms

def SiStripPopConPedestals(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConPedestals',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
