import FWCore.ParameterSet.Config as cms

def DD4hepTestG4Geometry(**kwargs):
  mod = cms.EDAnalyzer('DD4hepTestG4Geometry',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
