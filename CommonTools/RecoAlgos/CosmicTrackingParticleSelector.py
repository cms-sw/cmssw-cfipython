import FWCore.ParameterSet.Config as cms

def CosmicTrackingParticleSelector(*args, **kwargs):
  mod = cms.EDFilter('CosmicTrackingParticleSelector',
    src = cms.InputTag(''),
    ptMin = cms.double(0.9),
    minRapidity = cms.double(-2.4),
    maxRapidity = cms.double(2.4),
    tip = cms.double(100),
    lip = cms.double(100),
    minHit = cms.int32(0),
    chargedOnly = cms.bool(True),
    pdgId = cms.vint32(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
