import FWCore.ParameterSet.Config as cms

def Phase2PixelNtuple(**kwargs):
  mod = cms.EDAnalyzer('Phase2PixelNtuple',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
