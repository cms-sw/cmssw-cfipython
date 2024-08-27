import FWCore.ParameterSet.Config as cms

def MCParticleModuloFilter(**kwargs):
  mod = cms.EDFilter('MCParticleModuloFilter',
    moduleLabel = cms.InputTag('generator', 'unsmeared'),
    particleIDs = cms.vint32(),
    multipleOf = cms.uint32(1),
    absID = cms.bool(False),
    min = cms.uint32(0),
    status = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
