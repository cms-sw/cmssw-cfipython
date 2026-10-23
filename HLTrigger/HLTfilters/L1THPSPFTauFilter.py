import FWCore.ParameterSet.Config as cms

def L1THPSPFTauFilter(*args, **kwargs):
  mod = cms.EDFilter('L1THPSPFTauFilter',
    saveTags = cms.bool(True),
    MinPt = cms.double(-1),
    MinEta = cms.double(-5),
    MaxEta = cms.double(5),
    MaxRelChargedIso = cms.double(1000000000),
    MinLeadTrackPt = cms.double(-1),
    MinN = cms.int32(1),
    inputTag = cms.InputTag('L1HPSPFTaus'),
    Scalings = cms.PSet(
      barrel = cms.vdouble(
        0,
        1,
        0
      ),
      overlap = cms.vdouble(
        0,
        1,
        0
      ),
      endcap = cms.vdouble(
        0,
        1,
        0
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
