import FWCore.ParameterSet.Config as cms

def ParticleListDrawer(**kwargs):
  mod = cms.EDAnalyzer('ParticleListDrawer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
