import FWCore.ParameterSet.Config as cms

def StatusCandViewSelector(*args, **kwargs):
  mod = cms.EDFilter('StatusCandViewSelector',
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
