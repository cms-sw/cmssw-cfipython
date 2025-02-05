import FWCore.ParameterSet.Config as cms

def PhiRangeSelector(*args, **kwargs):
  mod = cms.EDFilter('PhiRangeSelector',
    src = cms.InputTag(''),
    phiMin = cms.double(-3.2),
    phiMax = cms.double(3.2),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
