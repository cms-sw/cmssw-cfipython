import FWCore.ParameterSet.Config as cms

def MCParticleModuloFilter(*args, **kwargs):
  mod = cms.EDFilter('MCParticleModuloFilter',
    moduleLabel = cms.InputTag('generator', 'unsmeared'),
    particleIDs = cms.vint32(),
    multipleOf = cms.uint32(1),
    absID = cms.bool(False),
    min = cms.uint32(0),
    status = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
