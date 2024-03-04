import FWCore.ParameterSet.Config as cms

def HGCalSimHitValidation(**kwargs):
  mod = cms.EDProducer('HGCalSimHitValidation',
    DetectorName = cms.string('HGCalEESensitive'),
    CaloHitSource = cms.string('HGCHitsEE'),
    TimeSlices = cms.vdouble(
      25,
      1000
    ),
    Verbosity = cms.untracked.int32(0),
    TestNumber = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
