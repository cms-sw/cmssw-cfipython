import FWCore.ParameterSet.Config as cms

def GenParticleCustomSelector(*args, **kwargs):
  mod = cms.EDFilter('GenParticleCustomSelector',
    src = cms.InputTag(''),
    ptMin = cms.double(0.9),
    minRapidity = cms.double(-2.4),
    maxRapidity = cms.double(2.4),
    tip = cms.double(3.5),
    lip = cms.double(30),
    chargedOnly = cms.bool(True),
    status = cms.int32(1),
    pdgId = cms.vint32(),
    invertRapidityCut = cms.bool(False),
    minPhi = cms.double(-3.2),
    maxPhi = cms.double(3.2),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
