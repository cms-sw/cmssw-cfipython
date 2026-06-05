import FWCore.ParameterSet.Config as cms

def L1TTkMuonFilter(*args, **kwargs):
  mod = cms.EDFilter('L1TTkMuonFilter',
    saveTags = cms.bool(True),
    MinPt = cms.double(-1),
    MinEta = cms.double(-5),
    MaxEta = cms.double(5),
    MinN = cms.int32(1),
    inputTag = cms.InputTag('L1TkMuons'),
    applyQuality = cms.bool(False),
    applyDuplicateRemoval = cms.bool(True),
    qualities = cms.vint32(),
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
