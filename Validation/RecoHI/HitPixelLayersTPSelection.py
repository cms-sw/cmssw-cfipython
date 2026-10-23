import FWCore.ParameterSet.Config as cms

def HitPixelLayersTPSelection(*args, **kwargs):
  mod = cms.EDFilter('HitPixelLayersTPSelection',
    src = cms.InputTag(''),
    tripletSeedOnly = cms.bool(True),
    ptMin = cms.double(2),
    minRapidity = cms.double(-2.5),
    maxRapidity = cms.double(2.5),
    tip = cms.double(3.5),
    lip = cms.double(30),
    minHit = cms.int32(8),
    signalOnly = cms.bool(False),
    chargedOnly = cms.bool(True),
    primaryOnly = cms.bool(True),
    tpStatusBased = cms.bool(True),
    pdgId = cms.vint32(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
