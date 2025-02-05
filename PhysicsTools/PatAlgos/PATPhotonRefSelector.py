import FWCore.ParameterSet.Config as cms

def PATPhotonRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATPhotonRefSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
