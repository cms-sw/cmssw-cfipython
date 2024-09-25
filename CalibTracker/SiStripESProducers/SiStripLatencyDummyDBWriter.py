import FWCore.ParameterSet.Config as cms

def SiStripLatencyDummyDBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripLatencyDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
