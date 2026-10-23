import FWCore.ParameterSet.Config as cms

def SiPixelFakeTemplateDBSourceReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeTemplateDBSourceReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
