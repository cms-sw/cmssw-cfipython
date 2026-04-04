import FWCore.ParameterSet.Config as cms

def CTPPSGeometryInfo(*args, **kwargs):
  mod = cms.EDAnalyzer('CTPPSGeometryInfo',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
