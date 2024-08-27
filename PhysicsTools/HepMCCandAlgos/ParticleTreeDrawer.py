import FWCore.ParameterSet.Config as cms

def ParticleTreeDrawer(**kwargs):
  mod = cms.EDAnalyzer('ParticleTreeDrawer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
