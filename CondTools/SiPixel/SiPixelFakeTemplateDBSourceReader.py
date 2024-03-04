import FWCore.ParameterSet.Config as cms

def SiPixelFakeTemplateDBSourceReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeTemplateDBSourceReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
