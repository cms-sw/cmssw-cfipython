import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelTemplateDBObjectReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
