import FWCore.ParameterSet.Config as cms

def SiPixelVCalReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelVCalReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
