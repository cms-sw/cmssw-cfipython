import FWCore.ParameterSet.Config as cms

def SiStripGainFromData(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainFromData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
