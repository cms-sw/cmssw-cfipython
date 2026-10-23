import FWCore.ParameterSet.Config as cms

def HFPreReconstructor(*args, **kwargs):
  mod = cms.EDProducer('HFPreReconstructor',
    digiLabel = cms.InputTag('hcalDigis'),
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    dropZSmarkedPassed = cms.bool(False),
    tsFromDB = cms.bool(False),
    sumAllTimeSlices = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
