import FWCore.ParameterSet.Config as cms

def PATPFParticleSelector(**kwargs):
  mod = cms.EDFilter('PATPFParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
