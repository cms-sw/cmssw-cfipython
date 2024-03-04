import FWCore.ParameterSet.Config as cms

def SiStripModuleTimer(**kwargs):
  mod = cms.EDAnalyzer('SiStripModuleTimer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
