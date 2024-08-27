import FWCore.ParameterSet.Config as cms

def CTPPSGeometryInfo(**kwargs):
  mod = cms.EDAnalyzer('CTPPSGeometryInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
