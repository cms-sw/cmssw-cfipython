import FWCore.ParameterSet.Config as cms

def CandSelector(*args, **kwargs):
  mod = cms.EDFilter('CandSelector',
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
