import FWCore.ParameterSet.Config as cms

def SiPixelDetInfoFileWriter(**kwargs):
  mod = cms.EDAnalyzer('SiPixelDetInfoFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
