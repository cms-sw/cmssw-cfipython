import FWCore.ParameterSet.Config as cms

def SiPixelTestSummary(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelTestSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
