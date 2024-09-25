import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixel2DTemplateDBObjectReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
