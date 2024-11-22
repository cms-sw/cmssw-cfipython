import FWCore.ParameterSet.Config as cms

def SiStripApvGainBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
