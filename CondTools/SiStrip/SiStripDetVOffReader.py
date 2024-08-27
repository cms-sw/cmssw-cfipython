import FWCore.ParameterSet.Config as cms

def SiStripDetVOffReader(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetVOffReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
