import FWCore.ParameterSet.Config as cms

def SiStripGainFromAsciiFile(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripGainFromAsciiFile',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
