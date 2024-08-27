import FWCore.ParameterSet.Config as cms

def CTPPSPixelDAQMappingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CTPPSPixelDAQMappingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
