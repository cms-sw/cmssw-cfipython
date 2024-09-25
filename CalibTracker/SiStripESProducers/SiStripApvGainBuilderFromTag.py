import FWCore.ParameterSet.Config as cms

def SiStripApvGainBuilderFromTag(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainBuilderFromTag',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
