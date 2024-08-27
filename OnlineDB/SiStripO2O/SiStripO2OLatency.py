import FWCore.ParameterSet.Config as cms

def SiStripO2OLatency(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OLatency',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
