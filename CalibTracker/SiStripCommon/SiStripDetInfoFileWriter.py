import FWCore.ParameterSet.Config as cms

def SiStripDetInfoFileWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDetInfoFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
