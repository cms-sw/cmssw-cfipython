import FWCore.ParameterSet.Config as cms

def SiStripApvGainBuilderFromTag(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainBuilderFromTag',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
