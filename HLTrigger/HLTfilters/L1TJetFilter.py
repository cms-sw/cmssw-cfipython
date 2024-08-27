import FWCore.ParameterSet.Config as cms

def L1TJetFilter(**kwargs):
  mod = cms.EDFilter('L1TJetFilter',
    saveTags = cms.bool(True),
    inputTag = cms.InputTag('ak4PFL1PuppiCorrected'),
    MinPt = cms.double(-1),
    MinEta = cms.double(-5),
    MaxEta = cms.double(5),
    MinN = cms.int32(1),
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
