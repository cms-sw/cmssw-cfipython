import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectUploader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelTemplateDBObjectUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
