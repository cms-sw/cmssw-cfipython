import FWCore.ParameterSet.Config as cms

def SiStripPopConThreshold(**kwargs):
  mod = cms.EDAnalyzer('SiStripPopConThreshold',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
