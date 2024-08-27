import FWCore.ParameterSet.Config as cms

def SiStripO2OApvGain(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2OApvGain',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
