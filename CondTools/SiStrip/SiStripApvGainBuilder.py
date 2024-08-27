import FWCore.ParameterSet.Config as cms

def SiStripApvGainBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainBuilder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
