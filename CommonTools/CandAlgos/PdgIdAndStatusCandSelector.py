import FWCore.ParameterSet.Config as cms

def PdgIdAndStatusCandSelector(*args, **kwargs):
  mod = cms.EDFilter('PdgIdAndStatusCandSelector',
    src = cms.InputTag(''),
    pdgId = cms.vint32(),
    status = cms.vint32(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
