import FWCore.ParameterSet.Config as cms

def CastorChannelQualityPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CastorChannelQualityPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
