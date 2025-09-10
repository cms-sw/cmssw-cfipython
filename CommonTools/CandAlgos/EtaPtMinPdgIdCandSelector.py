import FWCore.ParameterSet.Config as cms

def EtaPtMinPdgIdCandSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaPtMinPdgIdCandSelector',
    src = cms.InputTag(''),
    ptMin = cms.double(0),
    etaMin = cms.double(0),
    etaMax = cms.double(0),
    pdgId = cms.vint32(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
