import FWCore.ParameterSet.Config as cms

def SiStripPopConPedestals(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripPopConPedestals',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
