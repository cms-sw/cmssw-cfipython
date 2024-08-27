import FWCore.ParameterSet.Config as cms

def SiStripLatencyDummyDBWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripLatencyDummyDBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
