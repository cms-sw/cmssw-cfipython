import FWCore.ParameterSet.Config as cms

def SiStripGainFromAsciiFile(**kwargs):
  mod = cms.EDAnalyzer('SiStripGainFromAsciiFile',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
