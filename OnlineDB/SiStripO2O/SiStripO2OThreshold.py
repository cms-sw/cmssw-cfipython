import FWCore.ParameterSet.Config as cms

def SiStripO2OThreshold(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OThreshold',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
