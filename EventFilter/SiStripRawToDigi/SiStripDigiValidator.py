import FWCore.ParameterSet.Config as cms

def SiStripDigiValidator(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDigiValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
