import FWCore.ParameterSet.Config as cms

def MCDisplacementFilter(*args, **kwargs):
  mod = cms.EDFilter('MCDisplacementFilter',
    hepMCProductTag = cms.InputTag('generator', 'unsmeared'),
    ParticleIDs = cms.vint32(0),
    LengMax = cms.double(-1),
    LengMin = cms.double(-1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
