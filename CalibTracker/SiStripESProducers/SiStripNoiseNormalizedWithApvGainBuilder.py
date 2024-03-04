import FWCore.ParameterSet.Config as cms

def SiStripNoiseNormalizedWithApvGainBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripNoiseNormalizedWithApvGainBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
