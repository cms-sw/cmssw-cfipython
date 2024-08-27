import FWCore.ParameterSet.Config as cms

def BeamSplash(**kwargs):
  mod = cms.EDFilter('BeamSplash',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
