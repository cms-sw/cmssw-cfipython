import FWCore.ParameterSet.Config as cms

def PATPFParticleRefSelector(**kwargs):
  mod = cms.EDFilter('PATPFParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
