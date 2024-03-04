import FWCore.ParameterSet.Config as cms

def SiPixelGenErrorDBObjectUploader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelGenErrorDBObjectUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
