import FWCore.ParameterSet.Config as cms

def SiStripDetInfoFileWriter(**kwargs):
  mod = cms.EDAnalyzer('SiStripDetInfoFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
