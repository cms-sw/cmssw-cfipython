import FWCore.ParameterSet.Config as cms

def SiStripDigiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
