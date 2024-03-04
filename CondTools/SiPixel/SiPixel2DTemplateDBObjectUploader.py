import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectUploader(**kwargs):
  mod = cms.EDAnalyzer('SiPixel2DTemplateDBObjectUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
