import FWCore.ParameterSet.Config as cms

def SiPixelTemplateDBObjectReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelTemplateDBObjectReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
