import FWCore.ParameterSet.Config as cms

def SiPixelGenErrorDBObjectReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelGenErrorDBObjectReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
