import FWCore.ParameterSet.Config as cms

def SiPixelPerformanceSummaryReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelPerformanceSummaryReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
