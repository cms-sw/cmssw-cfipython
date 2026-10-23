import FWCore.ParameterSet.Config as cms

def SeedChargeSelector(*args, **kwargs):
  mod = cms.EDFilter('SeedChargeSelector',
    src = cms.InputTag(''),
    charge = cms.int32(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
