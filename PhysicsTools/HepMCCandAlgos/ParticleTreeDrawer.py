import FWCore.ParameterSet.Config as cms

def ParticleTreeDrawer(*args, **kwargs):
  mod = cms.EDAnalyzer('ParticleTreeDrawer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
