import FWCore.ParameterSet.Config as cms

def SiPixelTestSummary(**kwargs):
  mod = cms.EDAnalyzer('SiPixelTestSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
