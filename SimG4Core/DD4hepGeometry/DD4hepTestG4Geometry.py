import FWCore.ParameterSet.Config as cms

def DD4hepTestG4Geometry(*args, **kwargs):
  mod = cms.EDAnalyzer('DD4hepTestG4Geometry',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
