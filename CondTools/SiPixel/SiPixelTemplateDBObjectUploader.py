import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectUploader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelTemplateDBObjectUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
