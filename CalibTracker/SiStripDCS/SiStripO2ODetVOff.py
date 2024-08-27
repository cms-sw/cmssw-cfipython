import FWCore.ParameterSet.Config as cms

def SiStripO2ODetVOff(**kwargs):
  mod = cms.EDAnalyzer('SiStripO2ODetVOff',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
