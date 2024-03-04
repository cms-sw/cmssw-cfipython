import FWCore.ParameterSet.Config as cms

def MCDisplacementFilter(**kwargs):
  mod = cms.EDFilter('MCDisplacementFilter',
    hepMCProductTag = cms.InputTag('generator', 'unsmeared'),
    ParticleIDs = cms.vint32(0),
    LengMax = cms.double(-1),
    LengMin = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
