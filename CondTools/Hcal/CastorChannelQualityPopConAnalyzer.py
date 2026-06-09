import FWCore.ParameterSet.Config as cms

def CastorChannelQualityPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorChannelQualityPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
