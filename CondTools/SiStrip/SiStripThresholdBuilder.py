import FWCore.ParameterSet.Config as cms

def SiStripThresholdBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripThresholdBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
