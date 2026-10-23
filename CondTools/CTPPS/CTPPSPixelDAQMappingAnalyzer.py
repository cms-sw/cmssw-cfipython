import FWCore.ParameterSet.Config as cms

def CTPPSPixelDAQMappingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSPixelDAQMappingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
