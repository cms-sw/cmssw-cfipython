import FWCore.ParameterSet.Config as cms

def SiPixelDetInfoFileWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelDetInfoFileWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
