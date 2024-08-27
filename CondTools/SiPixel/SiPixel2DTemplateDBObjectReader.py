import FWCore.ParameterSet.Config as cms

def SiPixel2DTemplateDBObjectReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixel2DTemplateDBObjectReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
