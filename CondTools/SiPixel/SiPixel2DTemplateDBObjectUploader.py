import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectUploader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixel2DTemplateDBObjectUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
