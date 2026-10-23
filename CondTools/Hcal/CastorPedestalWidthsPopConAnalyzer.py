import FWCore.ParameterSet.Config as cms

def CastorPedestalWidthsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CastorPedestalWidthsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
