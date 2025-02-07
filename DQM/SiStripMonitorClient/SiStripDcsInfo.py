import FWCore.ParameterSet.Config as cms

def SiStripDcsInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDcsInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
