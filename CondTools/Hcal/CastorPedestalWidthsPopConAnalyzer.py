import FWCore.ParameterSet.Config as cms

def CastorPedestalWidthsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorPedestalWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
