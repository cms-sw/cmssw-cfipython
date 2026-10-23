import FWCore.ParameterSet.Config as cms

def SiStripQualityHotStripIdentifierRoot(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripQualityHotStripIdentifierRoot',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
