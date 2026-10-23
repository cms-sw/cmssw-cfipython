import FWCore.ParameterSet.Config as cms

def ParticleDecayDrawer(*args, **kwargs):
  mod = cms.EDAnalyzer('ParticleDecayDrawer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
