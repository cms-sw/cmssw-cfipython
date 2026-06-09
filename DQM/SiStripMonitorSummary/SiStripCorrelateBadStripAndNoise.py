import FWCore.ParameterSet.Config as cms

def SiStripCorrelateBadStripAndNoise(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripCorrelateBadStripAndNoise',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
