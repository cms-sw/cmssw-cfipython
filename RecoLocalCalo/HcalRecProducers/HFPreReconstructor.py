import FWCore.ParameterSet.Config as cms

def HFPreReconstructor(**kwargs):
  mod = cms.EDProducer('HFPreReconstructor',
    digiLabel = cms.required.InputTag,
    forceSOI = cms.int32(-1),
    soiShift = cms.int32(0),
    dropZSmarkedPassed = cms.required.bool,
    tsFromDB = cms.required.bool,
    sumAllTimeSlices = cms.required.bool,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
