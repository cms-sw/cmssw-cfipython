import FWCore.ParameterSet.Config as cms

def PATPFParticleSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPFParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod