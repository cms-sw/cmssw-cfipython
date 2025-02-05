import FWCore.ParameterSet.Config as cms

def StatusCandSelector(*args, **kwargs):
  mod = cms.EDFilter('StatusCandSelector',
    src = cms.InputTag(''),
    status = cms.vint32(),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
