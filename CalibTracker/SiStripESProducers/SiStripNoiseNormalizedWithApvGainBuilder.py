import FWCore.ParameterSet.Config as cms

def SiStripNoiseNormalizedWithApvGainBuilder(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoiseNormalizedWithApvGainBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
